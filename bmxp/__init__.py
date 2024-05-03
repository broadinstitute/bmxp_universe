# Feature Metadata
FMDATA = {
    # provided
    "Compound_ID": "Compound_ID",  # misnomer, project-unique feature ID
    "RT": "RT",  # unitless retention time, may or may not be scaled
    "MZ": "MZ",  # unsigned mass-to-charge ratio
    "Intensity": "Intensity",  # feature intensity
    "Annotation_ID": "Annotation_ID",  # method-unique annotation label
    "Adduct": "Adduct",  # the adduct form of the annotation
    "__annotation_id": "__annotation_id",  # globally unique annotation identifier
    "Metabolite": "Metabolite",  # preferred display/reporting name of metabolite
    "Non_Quant": "Non_Quant",  # boolean denoting that a feature is not quanitifiable
    # generated by gravity
    "Cluster_Num": "Cluster_Num",  # cluster number assigned during Gravity clustering
    "Cluster_Size": "Cluster_Size",  # number of members in the cluster
    # generated by blueshift
    "Batches Skipped": "Batches Skipped",  # batches that were skipped since there were no prefs
}

# injection or acquisition metadata
IMDATA = {
    "injection_id": "injection_id",  # injectionname, usually filename
    "broad_id": "broad_id",  # internal biospecimen label
    "program_id": "program_id",  # external biospecimen label
    "injection_type": "injection_type",  # type of injecction
    "comments": "comments",  # comments about the injection
    "column_number": "column_number",  # column number, in multi-column studies
    "injection_order": "injection_order",  # injection number, not skipping blanks or non-samples
    "batches": "batches",  # 'batch start' or 'batch end'
    # generated by blueshift
    "QCRole": "QCRole",  # "QC-drift_correction", "QC-pooled_ref", or "QC-not_used"
}

# sample metadata, not including
SMDATA = {
    "broad_id": "broad_id",  # internal biospecimen label
    "program_id": "program_id",  # external biospecimen label
}

# names of pooled reference injection types
POOL_INJ_TYPES = ("PREFA", "PREFB")
