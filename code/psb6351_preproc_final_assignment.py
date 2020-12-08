#!/usr/bin/env python

##### Setup parameters for slurm scheduling systems #####

#SBATCH --partition centos7_default-partition
#SBATCH --account acc_psb6351
#SBATCH --qos pq_psb6351
#SBATCH -o /scratch/hlee053/crash/preproc_o
#SBATCH -e /scratch/hlee053/crash/preproc_e

#########################################################

#### This pipeline consists of a series of sections: ####

# Import modules: to import necessary functions or modules
# Specify variables: to define variables which you use throughout the script
# Specify nodes: to creat some nodes to build a pipeline
# Specify workflows and connect nodes: to creat some workflows and specify the connections between the nodes and the workflows to be executed sequentially
# Input and output stream: to allow the computer to know the structure of your folders, where it can get the data from and where it should store the output data at
# Run workflow

#########################################################

#################### Import modules ####################

import os
from glob import glob
import pandas as pd
import numpy as np
import nipype.interfaces.afni as afni
import nipype.interfaces.fsl as fsl
import nipype.interfaces.freesurfer as fs
from nipype.interfaces.utility import Function
import nibabel as nb
import json
import nipype.interfaces.io as nio
import nipype.pipeline.engine as pe
import nipype.algorithms.rapidart as ra
import nipype.interfaces.utility as util

########################################################

################## Specify variables ###################

# Subjects List
sids = ['021']

# Experiment directory
base_dir = '/home/hlee053/Documents/mattfeld_2020'
work_dir = '/scratch/hlee053'
func_dir = os.path.join(base_dir, f'dset/sub-{sids[0]}/func')
fmap_dir = os.path.join(base_dir, f'dset/sub-{sids[0]}/fmap')
fs_dir = os.path.join(base_dir, 'derivatives', 'freesurfer')

# Get a list of the study task json and nifti converted files
func_json = sorted(glob(func_dir + '/*.json'))
func_files = sorted(glob(func_dir + '/*.nii.gz'))
fmap_files = sorted(glob(fmap_dir + '/*func*.nii.gz'))

# Function that eliminates the mapnode directory structure and assists in saving all of the outputs into a single directory
def get_subs(func_files):
    '''Produces Name Substitutions for Each Contrast'''
    subs = []
    for curr_run in range(len(func_files)):
        subs.append(('_tshifter%d' %curr_run, ''))
        subs.append(('_volreg%d' %curr_run, ''))
    return subs

# SUSAN funtions
def getbtthresh(medianvals):
    """Get the brightness threshold for SUSAN."""
    return [0.75*val for val in medianvals]

def getusans(inlist):
    """Return the usans at the right threshold."""
    return [[tuple([val[0],0.75*val[1]])] for val in inlist]

# Get aparc+aseg segmentation fucntion
def get_aparc_aseg(files):
    for name in files:
        if 'aparc+aseg' in name:
            return name
    raise ValueError('aparc+aseg.mgz not found')

# Finding a volumn having the minimum number of outliers by searching over the first 201 volumes
def best_vol(outlier_count):
    best_vol_num = outlier_count.index(min(outlier_count[:200]))
    if isinstance(best_vol_num, list):
        best_vol_num = best_vol_num[0] #pick the first one
    return best_vol_num

# Create a list of lists containing the slice timing for each study run
slice_timing_list = [] # define an empty list variable
for curr_json in func_json: # iterate over the variable func_json that was defined above through the sorted glob
    curr_json_data = open(curr_json) # open the json file
    curr_func_metadata = json.load(curr_json_data) # load the json file
    slice_timing_list.append(curr_func_metadata['SliceTiming'])

#########################################################

################# Create (map)nodes #####################
########## Specify workflows and connect nodes ##########

# Establish a nipype workflow to execute
psb6351_wf = pe.Workflow(name='psb6351_wf') # create a workflow
psb6351_wf.base_dir = work_dir + f'/psb6351workdir/sub-{sids[0]}' # deinfe the working directory where I want preliminary files to be written
psb6351_wf.config['execution']['use_relative_paths'] = True # assign a execution variable to use relative paths

# Create a Function node to substitute names of files created during pipeline
getsubs = pe.Node(Function(input_names=['func_files'],
                           output_names=['subs'],
                           function=get_subs),
                  name='getsubs')
getsubs.inputs.func_files = func_files

# Find the number of outliers at each volumn
# Serve as the base for the motion correction
id_outliers = pe.Node(afni.OutlierCount(),
                      name = 'id_outliers')
# Mandatory Inputs
id_outliers.inputs.in_file = func_files[0] # Input dataset # The 1st study run is the closest to structure scan
# Optional Inputs
id_outliers.inputs.automask = True # Clip off small voxels
id_outliers.inputs.fraction = True # Write out the fraction of masked voxels which are outliers at each timepoint
id_outliers.inputs.legendre = True # Use Legendre polynomials
id_outliers.inputs.polort = 4 # Detrend each voxel timeseries with polynomials of order 'integer' prior to outlier estimation # 4 is recommended
id_outliers.inputs.out_file = 'outlier_file'

# Create a Function node to identify the best volume based
getbestvol = pe.Node(Function(input_names=['outlier_count'],
                              output_names=['best_vol_num'],
                              function=best_vol),
                     name='getbestvol')
psb6351_wf.connect(id_outliers, 'out_file', getbestvol, 'outlier_count')

# Extract the earliest volume with the fewest outliers of the first run as the reference
extractref = pe.Node(fsl.ExtractROI(t_size=1),
                     name = "extractref")
extractref.inputs.in_file = func_files[0]
psb6351_wf.connect(getbestvol, 'best_vol_num', extractref, 't_min')

#Motion Correction
motion_correct =  pe.MapNode(fsl.MCFLIRT(save_mats = True,
                                         save_plots = True,
                                         interpolation = 'sinc'),
                             iterfield = ['in_file'],
                             name = 'motion_correct')

motion_correct.inputs.in_file = func_files
psb6351_wf.connect(extractref, 'roi_file', motion_correct, 'ref_file')

# Artifact Detection
artifactdetection = pe.MapNode(ra.ArtifactDetect(
                                        mask_type = 'spm_global',
                                        norm_threshold = 2,
                                        parameter_source = 'FSL',
                                        zintensity_threshold = 1),
                               iterfield = ['realigned_files', 'realignment_parameters'],
                               name = 'artifactdetection')
psb6351_wf.connect(motion_correct, 'par_file', artifactdetection, 'realignment_parameters')
psb6351_wf.connect(motion_correct, 'out_file', artifactdetection, 'realigned_files')

# Slicetiming Correction
tshifter = pe.MapNode(afni.TShift(),
                      iterfield=['in_file','slice_timing'],
                      name = 'tshifter')
tshifter.inputs.tr = '1.76'
tshifter.inputs.slice_timing = slice_timing_list
tshifter.inputs.outputtype = 'NIFTI_GZ'
psb6351_wf.connect(motion_correct, 'out_file', tshifter, 'in_file')

# Coregistration
# Calculate the transformation matrix from EPI space to FreeSurfer space
fs_register = pe.Node(fs.BBRegister(init='fsl'),
                      name ='fs_register')
fs_register.inputs.contrast_type = 't2'
fs_register.inputs.out_fsl_file = True
fs_register.inputs.subject_id = f'sub-{sids[0]}'
fs_register.inputs.subjects_dir = fs_dir
psb6351_wf.connect(extractref, 'roi_file', fs_register, 'source_file')

# Smoothing using SUSAN with the brightness threshold set to 75%
# of the median value for each run and a mask constituting the mean functional
smooth_median = pe.MapNode(fsl.ImageStats(op_string='-k %s -p 50'),
                           iterfield = ['in_file'],
                           name='smooth_median')
psb6351_wf.connect(maskfunc, 'out_file', smooth_median, 'in_file')
psb6351_wf.connect(fs_voltransform, 'transformed_file', smooth_median, 'mask_file')

# Calculate the mean functional
smooth_meanfunc = pe.MapNode(fsl.ImageMaths(op_string='-Tmean',
                                            suffix='_mean'),
                             iterfield=['in_file'],
                             name='smooth_meanfunc')
psb6351_wf.connect(maskfunc, 'out_file', smooth_meanfunc, 'in_file')

smooth_merge = pe.Node(util.Merge(2, axis='hstack'),
                       name='smooth_merge')
psb6351_wf.connect(smooth_meanfunc, 'out_file', smooth_merge, 'in1')
psb6351_wf.connect(smooth_median, 'out_stat', smooth_merge, 'in2')

# Below is the code for smoothing using the susan algorithm from FSL that
# limits smoothing based on different tissue classes
smooth = pe.MapNode(fsl.SUSAN(),
                    iterfield=['in_file', 'brightness_threshold', 'usans', 'fwhm'],
                    name='smooth')
smooth.inputs.fwhm=[4.0]
psb6351_wf.connect(maskfunc, 'out_file', smooth, 'in_file')
psb6351_wf.connect(smooth_median, ('out_stat', getbtthresh), smooth, 'brightness_threshold')
psb6351_wf.connect(smooth_merge, ('out', getusans), smooth, 'usans')

#########################################################

################ Input and output stream ################
datasink = pe.Node(nio.DataSink(), name="datasink")
datasink.inputs.base_directory = os.path.join(base_dir, 'derivatives/preproc')
datasink.inputs.container = f'sub-{sids[0]}'
psb6351_wf.connect(tshifter, 'out_file', datasink, 'sltime_corr')
psb6351_wf.connect(extractref, 'roi_file', datasink, 'study_ref')
###
psb6351_wf.connect(motion_correct, 'par_file', datasink, 'motion.@motion_parameters')
psb6351_wf.connect(motion_correct, 'out_file', datasink, 'motion.@realigned_files')
psb6351_wf.connect(artifactdetection, 'norm_files', datasink, 'artifactdetection.@artifact_norm_files')
psb6351_wf.connect(artifactdetection, 'outlier_files', datasink, 'artifactdetection.@artifact_outlier_files')
psb6351_wf.connect(artifactdetection, 'displacement_files', datasink, 'artifactdetection.@artifact_displacement_files')
###
psb6351_wf.connect(fs_register, 'out_reg_file', datasink, 'register.@reg_file')
psb6351_wf.connect(fs_register, 'min_cost_file', datasink, 'register.@reg_cost')
psb6351_wf.connect(fs_register, 'out_fsl_file', datasink, 'register.@reg_fsl_file')
psb6351_wf.connect(smooth, 'smoothed_file', datasink, 'funcsmoothed')
psb6351_wf.connect(getsubs, 'subs', datasink, 'substitutions')

#########################################################

#################### Run the workflow ###################

psb6351_wf.run(plugin='SLURM',
               plugin_args={'sbatch_args': ('--partition centos7_default-partition --qos pq_psb6351 --account acc_psb6351'),
                            'overwrite':True})

#########################################################
