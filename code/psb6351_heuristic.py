import os

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
    #use https://neuroimaging-core-docs.readthedocs.io/en/latest/pages/heudiconv.html tutorial

<<<<<<< HEAD
    #data = create_key('run{item:03d}')
    t1w = create_key('sub-{subject}/ses-S1/anat/sub-{subject}_ses-S1_run-{item}_T1w')
    dwi = create_key('sub-{subject}/ses-S1/dwi/sub-{subject}_ses-S1_run-{item}_dwi')
    ROI_loc1 = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-loc_run-{item}_bold')
    ROI_loc2 = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-loc_run-{item}_bold')
    study1 = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_run-{item}_bold')
    study2 = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_run-{item}_bold')
    study3 = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_run-{item}_bold')
    study4 = create_key('sub-{subject}/ses-S1/func/sub-{subject}_ses-S1_task-study_run-{item}_bold')
    fmri_map = create_key('sub-{subject}/ses-S1/fmap/sub-{subject}_ses-S1_acq-func_dir-{dir}_run-{item}_epi')
    dmri_map = create_key('sub-{subject}/ses-S1/fmap/sub-{subject}_ses-S1_acq-dwi_dir-{dir}_run-{item}_epi')

    
    info = {t1w : [], dwi : [], ROI_loc1 : [], ROI_loc2 : [], study1 : [], study2 : [], study3 : [], study4 : [], fmri_map : [], dmri_map : []}
   # last_run = len(seqinfo)

    for s in seqinfo:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now 
        * example_dcm_file
        * series_id
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

        #adding series id ?
        
        if (s.dim3 < 50) or (s.dim3 > 100) and ("T1w" in s.protocol_name):
            info[t1w].append({"item": s.series_id})
        elif (s.dim3 == 81) and (s.dim4 == 103) and ("dMRI" in s.protocol_name):
            info[dwi].append({"item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 304) and ("loc_1" in s.protocol_name):
            info[ROI_loc1].append({"item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 304) and ("loc_2" in s.protocol_name):
            info[ROI_loc2].append({"item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 355) and ("Study_1" in s.protocol_name):
            info[study1].append({"item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 355) and ("Study_2" in s.protocol_name):
            info[study2].append({"item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 355) and ("Study_3" in s.protocol_name):
            info[study3].append({"item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 355) and ("Study_4" in s.protocol_name):
            info[study4].append({"item": s.series_id})
        elif (s.dim3 == 81) and (s.dim4 == 1) and ("dMRI_DistortionMap_AP" in s.protocol_name):
            info[dmri_map].append({"dir": "AP", "item": s.series_id})
        elif (s.dim3 == 81) and (s.dim4 == 1) and ("dMRI_DistortionMap_PA" in s.protocol_name):
            info[dmri_map].append({"dir": "PA", "item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 1) and ("fMRI_DistortionMap_PA" in s.protocol_name):
            info[fmri_map].append({"dir": "PA", "item": s.series_id})
        elif (s.dim3 == 66) and (s.dim4 == 1) and ("fMRI_DistortionMap_AP" in s.protocol_name):
            info[fmri_map].append({"dir": "AP", "item": s.series_id})
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
>>>>>>> e611fba1650ba479e199cb1c0519dc3382bbc1d1
    return info
