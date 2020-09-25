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

    t1w = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/anat/sub-{subject}_T1w')
    dwi = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/dwi/sub-{subject}_dwi')
    func = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/func/sub-{subject}_task-REVL_acq-{rec}_bold')
    func_fmap = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/fmap/sub-{subject}_acq-func_dir-{dir}_run-{item}_epi')
    dwi_fmap = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/fmap/sub-{subject}_acq-dwi_dir-{dir}_run-{item}_epi')
    loc1 = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/func/sub-{subject}_task-loc_run-1_bold')
    loc2 = create_key('C:/Users/benji/OneDrive/Documentos/mattfeld_2020/dset/sub-{subject}/func/sub-{subject}_task-loc_run-2_bold')
    info = {t1w: [], dwi: [], func: [], func_fmap: [], dwi_fmap: [], loc1: [], loc2: []}
    last_run = len(seqinfo)

    for idx, s in enumerate (seqinfo):
        if (s.dim1 == 256) and (s.dim2 == 256) and (s.dim3 == 176) and (s.dim4 ==1) and ('T1w' in s.protocol_name):
            info[t1w] = [s.series_id]
        elif (s.dim1 == 140) and (s.dim2 == 140) and (s.dim3 == 81) and (s.dim4 ==103) and ('dMRI' in s.protocol_name):
            info[dwi] = [s.series_id]
        elif (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 ==355) and ('fMRI' in s.protocol_name):
            if ('_Study_1' in s.protocol_name):
                info[func].append({'rec':'Study_1'})
            elif ('_Study_2' in s.protocol_name):
                info[func].append({'rec':'Study_2'})
            elif ('_Study_3' in s.protocol_name):
                info[func].append({'rec':'Study_3'})
            else
                info[func].append({'rec':'Study_4'})
        elif (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 == 1) and ('DistortionMap' in s.protocol_name):
            if ('fMRI' in s.protocol_name) and ('PA' in s.protocol_name):
                info[func_fmap].append({'rec': 'func_fmap', 'dir': 'PA'})
            else ('fMRI' in s.protocol_name) and ('AP' in s.protocol_name):
                info[func_fmap].append({'rec': 'func_fmap', 'dir': 'AP'})
        elif (s.dim1 == 140) and (s.dim2 == 140) and (s.dim3 == 81) and (s.dim4 == 1) and ('DistortionMap' in s.protocol_name):
            if ('dMRI' in s.protocol_name) and ('AP' in s.protocol_name):
                info[dwi_fmap].append({'rec': 'dwi_fmap', 'dir': 'PA'})
            else ('dMRI' in s.protocol_name) and ('PA' in s.protocol_name):
                info[dwi_fmap].append({'rec': 'dwi_fmap', 'dir': 'PA'})        
        elif (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 ==304) and ('ROI_loc_1' in s.protocol_name):
            info[loc1] = [s.series_id]
        elif (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 ==304) and ('ROI_loc_2' in s.protocol_name):
            info[loc2] = [s.series_id]
    return info

