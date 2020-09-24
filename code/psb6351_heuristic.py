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
    """
    #use https://neuroimaging-core-docs.readthedocs.io/en/latest/pages/heudiconv.html tutorial

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
        
    return info
