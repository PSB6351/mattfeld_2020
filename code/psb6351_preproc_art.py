#!/usr/bin/env python

#SBATCH --partition centos7_16C_48G
#SBATCH --account acc_psb6351
#SBATCH --qos pq_psb6351
#SBATCH -o /scratch/madlab/Mattfeld_PSB6351/Vanessa/crash/preproc_art_o
#SBATCH -e /scratch/madlab/Mattfeld_PSB6351/Vanessa/crash/preproc_art_e

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
import nipype.interfaces.utility as util
import nipype.algorithms.rapidart as art

sids = ['021']

#Setting up directories
base_dir = '/home/mrive301/psb6351_data'
work_dir = '/scratch/madlab/Mattfeld_PSB6351/Vanessa'
func_dir = os.path.join(base_dir, f'dset/sub-{sids[0]}/func')
fmap_dir = os.path.join(base_dir, f'dset/sub-{sids[0]}/fmap')
fs_dir = os.path.join(base_dir, 'derivatives', 'freesurfer')

#Getting list of study task json and nifti converted files
func_json = sorted(glob(func_dir + '/*.json'))
func_files = sorted(glob(func_dir + '/*.nii.gz'))
fmap_files = sorted(glob(fmap_dir + '/*func*.nii.gz'))

#Eliminating mapnode directory to save outputs into 
    #a single directory 
def get_subs(func_files):
    '''Produces Name Substitutions for Each Contrast'''
    subs = []
    for curr_run in range(len(func_files)):
        subs.append(('_tshifter%d' %curr_run, ''))
        subs.append(('_volreg%d' %curr_run, ''))
        subs.append(('_smooth%d' %curr_run, ''))
    return subs

def getbtthresh(medianvals):
    """Get the brightness threshold for SUSAN."""
    return [0.75*val for val in medianvals]

def getusans(inlist):
    """Return the usans at the right threshold."""
    return [[tuple([val[0],0.75*val[1]])] for val in inlist]

def get_aparc_aseg(files):
    for name in files:
        if 'aparc+aseg' in name:
            return name
    raise ValueError('aparc+aseg.mgz not found')

#Inputing a text file that includes the number of outliers
#at each volume. We then find has the minimum number
#of outliers (e.g., min) by searching over the first 201 volumes
def best_vol(outlier_count):
    best_vol_num = outlier_count.index(min(outlier_count[:200]))
    #If the index function returns a list because there were
        #multiple volumes with the same outlier count, pick the first 
    if isinstance(best_vol_num, list):
        best_vol_num = best_vol_num[0]
    return best_vol_num

#Creating a list of lists containing the slice timing for each study run
slice_timing_list = []
for curr_json in func_json: 
    curr_json_data = open(curr_json)
    curr_func_metadata = json.load(curr_json_data) 
    slice_timing_list.append(curr_func_metadata['SliceTiming'])

#Creating workflow!
psb6351_wf = pe.Workflow(name='psb6351_wf') 
psb6351_wf.base_dir = work_dir + f'/psb6351workdir/sub-{sids[0]}' 
psb6351_wf.config['execution']['use_relative_paths'] = True 

# Create a function node to substitute names of files created during pipeline
getsubs = pe.Node(Function(input_names=['func_files'],
                           output_names=['subs'],
                           function=get_subs),
                  name='getsubs')
getsubs.inputs.func_files = func_files

#Using the first run of our functional data
#we use afni's 3dToutcount to find the number of 
# outliers at each volume. We will later select the
#earliest volume with the least number of outliers
#to serve as the base for the motion correction
id_outliers = pe.Node(afni.OutlierCount(),
                      name = 'id_outliers')
id_outliers.inputs.in_file = func_files[0]
id_outliers.inputs.automask = True
id_outliers.inputs.legendre = True
id_outliers.inputs.polort = 4
id_outliers.inputs.out_file = 'outlier_file'

# Create a function node to identify the best volume based
# on the number of outliers at each volume. 
getbestvol = pe.Node(Function(input_names=['outlier_count'],
                              output_names=['best_vol_num'],
                              function=best_vol),
                     name='getbestvol')
psb6351_wf.connect(id_outliers, 'out_file', getbestvol, 'outlier_count')

# Extracting the earliest volume of the first run as the reference 
extractref = pe.Node(fsl.ExtractROI(t_size=1),
                     name = "extractref")
extractref.inputs.in_file = func_files[0]
psb6351_wf.connect(getbestvol, 'best_vol_num', extractref, 't_min')

# Motion correct functional runs to the reference (1st volume of 1st run)
motion_correct =  pe.MapNode(fsl.MCFLIRT(save_mats = True,
                                         save_plots = True,
                                         interpolation = 'sinc'),
                             name = 'motion_correct',
                             iterfield = ['in_file'])
motion_correct.inputs.in_file = func_files
psb6351_wf.connect(extractref, 'roi_file', motion_correct, 'ref_file')

#Evaluating the number of outliers that are detected
    #when using zintensity of 1
    #and a norm_threshold of 0.2
art_detect = pe.MapNode(art.ArtifactDetect(use_differences = [True, False],
                                                                         zintensity_threshold = 1,
                                                                         mask_type = "spm_global",
                                                                         global_threshold = 8,
                                                                         norm_threshold = 0.2,
                                                                         parameter_source = 'FSL'),
                                                                         iterfield = ["realignment_parameters","realigned_files"],
                                                                         name="art_detect")
psb6351_wf.connect(motion_correct, 'par_file', art_detect, 'realignment_parameters')
psb6351_wf.connect(motion_correct, 'out_file', art_detect, 'realigned_files')

#Performing slice timing correction
tshifter = pe.MapNode(afni.TShift(),
                      iterfield=['in_file','slice_timing'],
                      name = 'tshifter')
tshifter.inputs.tr = '1.76'
tshifter.inputs.slice_timing = slice_timing_list
tshifter.inputs.outputtype = 'NIFTI_GZ'
psb6351_wf.connect(motion_correct, 'out_file', tshifter, 'in_file')

#Calculating the transformation matrix from EPI space to FS space
    #using the BBRegister command
fs_register = pe.Node(fs.BBRegister(init='fsl'),
                      name ='fs_register')
fs_register.inputs.contrast_type = 't2'
fs_register.inputs.out_fsl_file = True
fs_register.inputs.subject_id = f'sub-{sids[0]}'
fs_register.inputs.subjects_dir = fs_dir
psb6351_wf.connect(extractref, 'roi_file', fs_register, 'source_file')

#Registering a source file to fs space and creating a brain mask in source space
fssource = pe.Node(nio.FreeSurferSource(),
                   name ='fssource')
fssource.inputs.subject_id = f'sub-{sids[0]}'
fssource.inputs.subjects_dir = fs_dir

# Extracting aparc+aseg brain mask, binarize, and dilate by 1 voxel
fs_threshold = pe.Node(fs.Binarize(min=0.5, out_type='nii'),
                       name ='fs_threshold')
fs_threshold.inputs.dilate = 1
psb6351_wf.connect(fssource, ('aparc_aseg', get_aparc_aseg), fs_threshold, 'in_file')

#Transform the binarized aparc+aseg file to the EPI space
    #use a nearest neighbor interpolation
fs_voltransform = pe.Node(fs.ApplyVolTransform(inverse=True),
                          name='fs_transform')
fs_voltransform.inputs.subjects_dir = fs_dir
fs_voltransform.inputs.interp = 'nearest'
psb6351_wf.connect(extractref, 'roi_file', fs_voltransform, 'source_file')
psb6351_wf.connect(fs_register, 'out_reg_file', fs_voltransform, 'reg_file')
psb6351_wf.connect(fs_threshold, 'binary_file', fs_voltransform, 'target_file')

# Mask the functional runs with the extracted mask
maskfunc = pe.MapNode(fsl.ImageMaths(suffix='_bet',
                                     op_string='-mas'),
                      iterfield=['in_file'],
                      name = 'maskfunc')
psb6351_wf.connect(tshifter, 'out_file', maskfunc, 'in_file')
psb6351_wf.connect(fs_voltransform, 'transformed_file', maskfunc, 'in_file2')

# Smooth each run using SUSAn with the brightness threshold set to 75%
    #of the median value for each run and a mask constituting the mean functional
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

#Below is the code for smoothing using the susan algorithm from FSL that
    #limits smoothing based on different tissue classes
smooth = pe.MapNode(fsl.SUSAN(),
                    iterfield=['in_file', 'brightness_threshold', 'usans', 'fwhm'],
                    name='smooth')
smooth.inputs.fwhm=[4.0]
psb6351_wf.connect(maskfunc, 'out_file', smooth, 'in_file')
psb6351_wf.connect(smooth_median, ('out_stat', getbtthresh), smooth, 'brightness_threshold')
psb6351_wf.connect(smooth_merge, ('out', getusans), smooth, 'usans')

#Data sinking
datasink = pe.Node(nio.DataSink(), name="datasink")
datasink.inputs.base_directory = os.path.join(base_dir, 'derivatives/preproc_art4')
datasink.inputs.container = f'sub-{sids[0]}'
psb6351_wf.connect(tshifter, 'out_file', datasink, 'sltime_corr')
psb6351_wf.connect(extractref, 'roi_file', datasink, 'study_ref')
psb6351_wf.connect(motion_correct, 'par_file', datasink, 'motion.@motion_parameters')
psb6351_wf.connect(motion_correct, 'out_file', datasink, 'motion.@realigned_files')
psb6351_wf.connect(art_detect, 'norm_files', datasink, 'art_detect.@norm_files')
psb6351_wf.connect(art_detect, 'outlier_files', datasink, 'art_detect.@outlier_files')
psb6351_wf.connect(art_detect, 'displacement_files', datasink, 'art_detect.@displacement_files')
psb6351_wf.connect(fs_register, 'out_reg_file', datasink, 'register.@reg_file')
psb6351_wf.connect(fs_register, 'min_cost_file', datasink, 'register.@reg_cost')
psb6351_wf.connect(fs_register, 'out_fsl_file', datasink, 'register.@reg_fsl_file')
psb6351_wf.connect(smooth, 'smoothed_file', datasink, 'funcsmoothed')
psb6351_wf.connect(getsubs, 'subs', datasink, 'substitutions')

psb6351_wf.run(plugin='SLURM',
               plugin_args={'sbatch_args': ('--partition centos7_default-partition --qos pq_psb6351 --account acc_psb6351'),
                            'overwrite':True})

