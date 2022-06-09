#!/usr/bin/env python3

from __future__ import annotations

import warnings as _warnings
from typing import Any

import linear_operator

from . import deprecation, errors, grid, interpolation, quadrature, transforms, warnings
from .memoize import cached

__all__ = [
    "cached",
    "deprecation",
    "errors",
    "grid",
    "interpolation",
    "quadrature",
    "transforms",
    "warnings",
]


def __getattr__(name: str) -> Any:
    if hasattr(linear_operator.utils, name):
        _warnings.warn(
            f"gpytorch.utils.{name} is deprecated. Use linear_operator.utils.{name} instead.",
            DeprecationWarning,
        )
        return getattr(linear_operator.utils, name)
    raise AttributeError(f"module gpytorch.utils has no attribute {name}")
