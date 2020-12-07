import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """
    =========================================================
    Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    =========================================================
    """
    #Path to t1* and dwi:
        #"item" allows us to increment for every file (2 in the case of t1 (Nav & Nav_setter*)
    T1w = create_key('sub-{subject}/anat/sub-{subject}_run-{item}_T1w')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_run-{item}_dwi')
    #Paths to Study Tasks:
    Study1_task = create_key('sub-{subject}/func/sub-{subject}_task-study1_run-1_bold')
    Study2_task = create_key('sub-{subject}/func/sub-{subject}_task-study2_run-2_bold')
    Study3_task = create_key('sub-{subject}/func/sub-{subject}_task-study3_run-3_bold')
    Study4_task = create_key('sub-{subject}/func/sub-{subject}_task-study4_run-4_bold')
    #Paths to Task Localizers (1 and 2):
        #Not adding the 
    localizer1_task = create_key('sub-{subject}/func/sub-{subject}_localizer1_task_run-1_bold')
    localizer2_task = create_key('sub-{subject}/func/sub-{subject}_localizer2_task_run-2_bold')
    #Paths to Fieldmaps (functional and dwi):
        #"direct" will specify the AP or PA direction of fieldmaps. The "item" allows us to increment for every fieldmap
        #while specifying the direction. 
    func_fieldmap = create_key('sub-{subject}/fmap/sub-{subject}_acq-func_direction{direct}_run-{item}_fieldmap')
    dwi_fieldmap = create_key('sub-{subject}/fmap/sub-{subject}_acq-dwi_direction{direct}_run-{item}_fieldmap')
    
    #creating dictionary
    info = {T1w: [], dwi: [], Study1_task: [], Study2_task: [], 
                Study3_task: [], Study4_task: [], localizer1_task: [], 
                localizer2_task: [], func_fieldmap: [], dwi_fieldmap: []}
    
    #dimension 3 = slice time
    #dimension 4 = time point
    for s in seqinfo:
        if s.dim3 == 176 and s.dim4 == 1 and ("T1w_MPR_vNav" in s.series_description):
            info[T1w].append(s[2])
        elif s.dim4 == 355 and ('fMRI_REVL_Study_1' in s.series_description):
            info[Study1_task].append(s[2])
        elif s.dim4 == 355 and ('fMRI_REVL_Study_2' in s.series_description):
            info[Study2_task].append(s[2])
        elif s.dim4 == 355 and ('fMRI_REVL_Study_3' in s.series_description):
            info[Study3_task].append(s[2])
        elif s.dim4 == 355 and ('fMRI_REVL_Study_4' in s.series_description):
            info[Study4_task].append(s[2])
        #the next 2 localizers have the same dim3 and dim4 values
        #so specifying the series_description is sufficient
        elif 'fMRI_REVL_ROI_loc_1' in s.series_description:
            info[localizer1_task].append(s[2])
        elif 'fMRI_REVL_ROI_loc_2' in s.series_description:
            info[localizer2_task].append(s[2])
        elif s.dim4 == 103 and ('dMRI' in s.series_description):
            info[dwi].append(s[2])
        #the next 2 functional fieldmaps have the same dim3 and dim4 values
        #so specifying the series_description is sufficient
        elif "fMRI_DistortionMap_AP" in s.series_description:
            #we need to append a dictionary within the main dictionary
            #to account for the two strings we need to fill in
            #(i.e., item and direct)
            info[func_fieldmap].append({"item": s[2], "direct": "AP"})
        elif "fMRI_DistortionMap_PA" in s.series_description:
            info[func_fieldmap].append({"item": s[2], "direct": "PA"})
        #the next 2 dwi fieldmaps have the same dim3 and dim4 values
        #so specifying the series_description is sufficient
        elif "dMRI_DistortionMap_AP_dMRI_REVL" in s.series_description:
            info[dwi_fieldmap].append({"item": s[2], "direct": "AP"})
        elif "dMRI_DistortionMap_PA_dMRI_REVL" in s.series_description:
            info[dwi_fieldmap].append({"item": s[2], "direct": "PA"})
        else:
            pass
    return info
    
