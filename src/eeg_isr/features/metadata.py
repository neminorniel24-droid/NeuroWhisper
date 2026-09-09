"""Metadata definitions for EEG features."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureMetadata:
    name: str
    family: str
    description: str = ""


DEFAULT_FEATURE_METADATA = (
    FeatureMetadata("mean", "statistical", "Arithmetic mean"),
    FeatureMetadata("absmean", "statistical", "Mean absolute value"),
    FeatureMetadata("maximum", "statistical", "Maximum value"),
    FeatureMetadata("absmax", "statistical", "Maximum absolute value"),
    FeatureMetadata("minimum", "statistical", "Minimum value"),
)


def feature_names() -> tuple[str, ...]:
    return tuple(item.name for item in DEFAULT_FEATURE_METADATA)


def feature_families() -> tuple[str, ...]:
    return tuple(item.family for item in DEFAULT_FEATURE_METADATA)
