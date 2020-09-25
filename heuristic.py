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

    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_dwi')
    func = create_key('sub-{subject}/func/sub-{subject}_task-REVL_acq-{rec}_bold')
    fmap = create_key('sub-{subject}/fmap/sub-{subject}_acq-{rec}_dir-{dir}')
    localize = create_key('sub-{subject}/func/sub-{subject}_task-REVL_acq-{rec}_{loc}_bold')

    info = {t1w: [], dwi: [], func: [], fmap: [], localize: []}

    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 256) and (s.dim2 == 256) and (s.dim3 == 176) and (s.dim4 == 1) and ('T1w' in s.protocol_name):
            info[t1w] = [s.series_id]
        if (s.dim1 == 140) and (s.dim2 == 140) and (s.dim3 == 81) and (s.dim4 == 103) and ('dMRI' in s.protocol_name):
            info[dwi] = [s.series_id]
        if (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 == 355) and ('fMRI' in s.protocol_name):
            if ('_Study_1' in s.protocol_name):
                info[func].append({'rec': 'Study_1'})
            if ('_Study_2' in s.protocol_name):
                info[func].append({'rec': 'Study_2'})
            if ('_Study_3' in s.protocol_name):
                info[func].append({'rec': 'Study_3'})
            if ('_Study_4' in s.protocol_name):
                info[func].append({'rec': 'Study_4'})
        if (s.dim4 == 1) and ('DistortionMap' in s.protocol_name):
            if ('fMRI' in s.protocol_name) and ('PA' in s.protocol_name):
                info[fmap].append({'rec': 'func', 'dir': 'PA'})
            if ('fMRI' in s.protocol_name) and ('AP' in s.protocol_name):
                info[fmap].append({'rec': 'func', 'dir': 'AP'})
            if ('dMRI' in s.protocol_name) and ('PA' in s.protocol_name):
                info[fmap].append({'rec': 'dwi', 'dir': 'PA'})
            if ('dMRI' in s.protocol_name) and ('AP' in s.protocol_name):
                info[fmap].append({'rec': 'dwi', 'dir': 'AP'})
        if (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 == 304) and ('ROI' in s.protocol_name):
            if ("_loc_1" in s.protocol_name):
                info[localize].append({'rec': 'localizer', 'loc': 'loc_1'})
            else:
                info[localize].append({'rec': 'localizer', 'loc': 'loc_2'})

    return info
