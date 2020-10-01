# {item} # Convert DICOMs to BIDS-compatible dataset

import os

<<<<<<< HEAD
# create_key(template, outtype) -> A common helper function used to create the conversion key in infotodict
# infotodict(sequinfo) -> define the conversion outputs and specify the criteria for scan to output association
# For more infomation, visit https://heudiconv.readthedocs.io/en/latest/heuristics.html

=======
>>>>>>> upstream/master
def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    session: ses-[sessionID]
    bids_subject_session_dir: BIDS subject/session directory
    bids_subject_session_prefix: BIDS subject/session prefix
    """

<<<<<<< HEAD
# https://neuroimaging-core-docs.readthedocs.io/en/lastest/pages/heudiconv.htmal tutorial

# There is no definition of "subject" and "item" so I have no idea how "item" to be run in this file..(also {dir})
# I know there is only one subject {subject}, so I put this number to this script

# paths done in BIDS format
# data = create_key('run{item:03d}')

    # T1-weighted and Diffusion-weighted MRI
        # t1w = create_key('sub-{subject}/ses-S1/anat/sub-{subject}_run-{item}_T1w')
        # dwi = create_key('sub-{subject}/ses-S1/dwi/sub-{subject}_run-{item}_dwi')

    # ROI Localization
        # loc1_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_task-loc_run-1_bold')
        # loc2_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_task-loc_run-2_bold')

    # Study task
        # study1_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_task-study_run-1_bold')
        # study2_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_task-study_run-2_bold')
        # study3_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_task-study_run-3_bold')
        # study4_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_task-study_run-4_bold')

    # Fieldmaps of functional and dwi:
    # Direction({dir}) specifies the AP or PA direction of fieldmaps.
        # task_fmap = create_key('sub-{subject}/ses-S1/fmap/sub-{subject}_acq-func_dir-{dir}_run{item}_epi')
        # dwi_fmap = create_key('sub-{subject}/ses-S1/fmap/sub-{subject}_acq-dwi_dir-{dir}_run{item}_epi')


    t1w = create_key('sub-{subject}/ses-S1/anat/sub-{subject}_ses-S1_run-{item}_T1w')
    dwi = create_key('sub-{subject}/ses-S1/dwi/sub-{subject}_ses-S1_run-{item}_dwi')
    loc1_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-loc_{item}_bold')
    loc2_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-loc_{item}_bold')
    study1_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_{item}_bold')
    study2_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_{item}_bold')
    study3_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_{item}_bold')
    study4_task = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_{item}_bold')
    task_fmap = create_key('sub-{subject}/ses-S1/fmap/sub-{subject}_ses-S1_acq-func_dir-{dir}_run{item}_epi')
    dwi_fmap = create_key('sub-{subject}/ses-S1/fmap/sub-{subject}_ses-S1_acq-dwi_dir-{dir}_run{item}_epi')



# Dictionary for the dataset
# info = {data: []}
    info = {t1w: [], dwi: [], loc1_task: [], loc2_task: [],
            study1_task: [], study2_task: [], study3_task: [], study4_task: [],
            task_fmap: [], dwi_fmap: []}

    # last_run = len(seqinfo)



# dim3 = slice_num
# dim4 = timepoints

    for s in seqinfo:   # each row of dicominfo.tsv
        xdim, ydim, slice_num, timepoints = (s[6], s[7], s[8], s[9])  # What does mean the number in s[]? It's series_id
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now = s[0]
        * example_dcm_file = s[1]
        * series_id = s[2]...
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """

# info[data].append({"item": s.series_id})
# append() -> add a single item to the end of the existing list

    # T1-weighted and Diffusion-weighted MRI
        # if (slice_num == 176) and (timepoints == 1) and ("T1w_MPR_vNav" in s.series_description):
        #     info[t1w].append(s[2]) # I know the number in square brackets means 'series_id' but it seems it doesn't match with 'seris_id' of the dataset..
        # elif (slice_num > 1) and (timepoints == 103) and ("dMRI" in s[12]):
        #     info[dwi].append(s[2])

    # ROI Localization
        # elif (timepoints == 304) and ("ROI_loc_1" in s[12]):
        #     info[loc1_task].append(s[2])
        # elif (timepoints == 304) and ("ROI_loc_2" in s[12]):
        #     info[loc2_task].append(s[2])

    # Study task
        # elif (timepoints == 355) and ('Study_1' in s[12]):
        #     info[study1_task].append(s[2])
        # elif (timepoints == 355) and ('Study_2' in s[12]):
        #     info[study2_task].append(s[2])
        # elif (timepoints == 355) and ('Study_3' in s[12]):
        #     info[study3_task].append(s[2])
        # elif (timepoints == 355) and ('Study_4' in s[12]):
        #     info[study4_task].append(s[2])

    # Fieldmaps of functional and dwi:
        # elif "dMRI_DistortionMap_AP" in s.series_description:
        #     info[dwi_fmap].append({"item": s[2], "dir": "AP"})
        # elif "dMRI_DistortionMap_PA" in s.series_description:
        #     info[dwi_fmap].append({"item": s[2], "dir": "PA"})
        # elif "fMRI_DistortionMap_PA" in s.series_description:
        #     info[task_fmap].append({"item": s[2], "dir": "PA"})
        # elif "fMRI_DistortionMap_AP" in s.series_description:
        #     info[task_fmap].append({"item": s[2], "dir": "AP"})

        # else:
        #     pass

        if (s.dim3 == 176) and (s.dim4 == 1) and ("T1w_MPR_vNav" in s.series_description):
            info[t1w].append({"item": s.series_id})
        elif (s.dim3 > 1) and (s.dim4 == 103) and ("dMRI_AP_REVL" in s.series_description):
            info[dwi].append({"item": s.series_id})
        elif (s.dim4 == 304) and ("fMRI_REVL_ROI_loc_1" in s.series_description):
            info[loc1_task].append({"item": s.series_id})
        elif (s.dim4 == 304) and ("fMRI_REVL_ROI_loc_2" in s.series_description):
            info[loc2_task].append({"item": s.series_id})
        elif (s.dim4 == 355) and ("fMRI_REVL_Study_1" in s.series_description):
            info[study1_task].append({"item": s.series_id})
        elif (s.dim4 == 355) and ("fMRI_REVL_Study_2" in s.series_description):
            info[study2_task].append({"item": s.series_id})
        elif (s.dim4 == 355) and ("fMRI_REVL_Study_3" in s.series_description):
            info[study3_task].append({"item": s.series_id})
        elif (s.dim4 == 355) and ("fMRI_REVL_Study_4" in s.series_description):
            info[study4_task].append({"item": s.series_id})
        elif "dMRI_DistortionMap_AP_dMRI_REVL" in s.series_description:
            info[dwi_fmap].append({"dir": "AP", "item": s.series_id})
        elif "dMRI_DistortionMap_PA_dMRI_REVL" in s.series_description:
            info[dwi_fmap].append({"dir": "PA", "item": s.series_id})
        elif "fMRI_DistortionMap_PA" in s.series_description:
            info[task_fmap].append({"dir": "PA", "item": s.series_id})
        elif "fMRI_DistortionMap_AP" in s.series_description:
            info[task_fmap].append({"dir": "AP", "item": s.series_id})
        else:
            pass

=======
    t1w = create_key('sub-{subject}/anat/sub-{subject}_run-{item}_T1w')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_run-{item}_dwi')
    loc1_task = create_key('sub-{subject}/func/sub-{subject}_task-loc_run-1_bold')
    loc2_task = create_key('sub-{subject}/func/sub-{subject}_task-loc_run-2_bold')
    study1_task = create_key('sub-{subject}/func/sub-{subject}_task-study_run-1_bold')
    study2_task = create_key('sub-{subject}/func/sub-{subject}_task-study_run-2_bold')
    study3_task = create_key('sub-{subject}/func/sub-{subject}_task-study_run-3_bold')
    study4_task = create_key('sub-{subject}/func/sub-{subject}_task-study_run-4_bold')
    task_fmap = create_key('sub-{subject}/fmap/sub-{subject}_acq-func_dir-{dir}_run{item}_epi')
    dwi_fmap = create_key('sub-{subject}/fmap/sub-{subject}_acq-dwi_dir-{dir}_run{item}_epi')

    info = {t1w : [],
            dwi : [],
            loc1_task : [],
            loc2_task : [],
            study1_task : [],
            study2_task : [],
            study3_task : [],
            study4_task : [],
            task_fmap : [],
            dwi_fmap : []}

    for s in seqinfo:
        xdim, ydim, slice_num, timepoints = (s[6], s[7], s[8], s[9])
        if (slice_num == 176) and (timepoints == 1) and ("T1w_MPR_vNav" in s.series_description):
            info[t1w].append(s[2])
        elif (slice_num > 1) and (timepoints == 103) and ("dMRI" in s[12]):
            info[dwi].append(s[2])
        elif (timepoints == 304) and ("ROI_loc_1" in s[12]):
            info[loc1_task].append(s[2])
        elif (timepoints == 304) and ("ROI_loc_2" in s[12]):
            info[loc2_task].append(s[2])
        elif (timepoints == 355) and ('Study_1' in s[12]):
            info[study1_task].append(s[2])
        elif (timepoints == 355) and ('Study_1' in s[12]):
            info[study1_task].append(s[2])
        elif (timepoints == 355) and ('Study_2' in s[12]):
            info[study2_task].append(s[2])
        elif (timepoints == 355) and ('Study_3' in s[12]):
            info[study3_task].append(s[2])
        elif (timepoints == 355) and ('Study_4' in s[12]):
            info[study4_task].append(s[2])
        elif "dMRI_DistortionMap_AP" in s.series_description:
            info[dwi_fmap].append({"item": s[2], "dir": "AP"})
        elif "dMRI_DistortionMap_PA" in s.series_description:
            info[dwi_fmap].append({"item": s[2], "dir": "PA"})
        elif "fMRI_DistortionMap_PA" in s.series_description:
            info[task_fmap].append({"item": s[2], "dir": "PA"})
        elif "fMRI_DistortionMap_AP" in s.series_description:
            info[task_fmap].append({"item": s[2], "dir": "AP"})
        else:
            pass
>>>>>>> upstream/master
    return info
