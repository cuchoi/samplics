from samplics.categorical import CrossTabulation, Tabulation, Ttest
from samplics.datasets.datasets import (
    load_auto,
    load_birth,
    load_county_crop,
    load_county_crop_means,
    load_expenditure_milk,
    load_nhanes2,
    load_nhanes2brr,
    load_nhanes2jk,
    load_nmihs,
    load_psu_frame,
    load_psu_sample,
    load_ssu_sample,
)
from samplics.estimation import ReplicateEstimator, TaylorEstimator
from samplics.regression import SurveyGLM
from samplics.sae import EblupAreaModel, EblupUnitModel, EbUnitModel, EllUnitModel
from samplics.sampling import (
    SampleSelection,
    SampleSize,
    SampleSizeMeanOneSample,
    SampleSizeMeanTwoSample,
    SampleSizePropOneSample,
    SampleSizePropTwoSample,
    allocate,
    calculate_power,
    calculate_power_prop,
    calculate_ss_fleiss_prop,
    calculate_ss_wald_prop,
    calculate_ss_wald_mean,
    power_for_one_mean,
    power_for_one_proportion,
)
from samplics.utils import array_to_dict, PopParam, SizeMethod, transform

from samplics.weighting import ReplicateWeight, SampleWeight


__all__ = [
    "allocate",
    "array_to_dict",
    "calculate_power",
    "calculate_power_prop",
    "calculate_ss_fleiss_prop",
    "calculate_ss_wald_prop",
    "calculate_ss_wald_mean",
    "CrossTabulation",
    "Tabulation",
    "Ttest",
    "EblupAreaModel",
    "EblupUnitModel",
    "EbUnitModel",
    "EllUnitModel",
    "load_auto",
    "load_birth",
    "load_county_crop",
    "load_county_crop_means",
    "load_expenditure_milk",
    "load_nhanes2",
    "load_nhanes2brr",
    "load_nhanes2jk",
    "load_nmihs",
    "load_psu_frame",
    "load_psu_sample",
    "load_ssu_sample",
    "PopParam",
    "power_for_one_mean",
    "power_for_one_proportion",
    "SampleSelection",
    "SampleSize",
    "SampleSizeMeanOneSample",
    "SampleSizeMeanTwoSample",
    "SampleSizePropOneSample",
    "SampleSizePropTwoSample",
    "SampleWeight",
    "SizeMethod",
    "SurveyGLM",
    "ReplicateWeight",
    "ReplicateEstimator",
    "TaylorEstimator",
    "transform",
]

__version__ = "0.3.38"
