"""Instance size test case."""
from __future__ import annotations

import pytest

from aws_instance_type_comparator.instance_type import InstanceSize


def test_init() -> None:
    """Initialize test."""
    sz1 = InstanceSize("large")
    assert str(sz1) == "large"
    with pytest.raises(ValueError):
        InstanceSize("hoge")


def test_eq() -> None:
    """Equal test."""
    sz1 = InstanceSize("large")
    sz2 = InstanceSize("large")
    sz3 = InstanceSize("2xlarge")
    assert sz1 == sz2
    assert not (sz1 == sz3)


def test_ne() -> None:
    """Not equal test."""
    sz1 = InstanceSize("large")
    sz2 = InstanceSize("large")
    sz3 = InstanceSize("2xlarge")
    assert not (sz1 != sz2)
    assert sz1 != sz3


def test_lt() -> None:
    """Lesser than test."""
    sz1 = InstanceSize("large")
    sz2 = InstanceSize("large")
    sz3 = InstanceSize("2xlarge")
    sz4 = InstanceSize("micro")
    sz5 = InstanceSize("metal")
    sz6 = InstanceSize("metal-24xl")
    sz7 = InstanceSize("metal-48xl")
    assert not sz1 < sz2
    assert sz1 < sz3
    assert not sz1 < sz4
    assert sz1 < sz5
    assert sz1 < sz6
    assert not sz3 < sz4
    assert sz4 < sz3
    assert sz3 < sz5
    assert sz3 < sz6
    assert sz5 < sz6
    assert sz6 < sz7
