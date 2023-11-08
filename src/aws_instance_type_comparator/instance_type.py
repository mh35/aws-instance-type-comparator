"""Instance type classes definition."""
from __future__ import annotations

import re
from enum import Enum


# General


class InstanceService(str, Enum):
    """Service for instance type."""

    EC2 = "ec2"
    CLOUDSEARCH = "cloudsearch"
    OPENSEARCH = "opensearch"
    KAFKA = "kafka"
    MQ = "mq"
    SIMSPACE = "sim"
    DATABASE = "db"  # RDS, DocumentDB, MemoryDB for Redis, Neptune
    ELASTICACHE = "cache"
    SAGEMAKER = "ml"
    MAINFRAME_MODERNIZATION = "M2"
    BRACKET_TRAINING = "ml-Training"


_FIXED_INSTANCE_TYPES = ["nano", "micro", "small", "medium", "large"]


class InstanceSize:
    """Instance size."""

    def __init__(self: InstanceSize, name: str) -> None:
        """Initialize instance size data.

        Args:
            name(str): Instance size name

        Raises:
            ValueError: If instance size name is invalid
        """
        if name in _FIXED_INSTANCE_TYPES:
            self._name = name
            self._size_value: int = 2 ** _FIXED_INSTANCE_TYPES.index(name)
            self._is_metal = False
            return
        if name == "metal":
            self._name = name
            self._size_value = 1
            self._is_metal = True
            return
        metal_md = re.match(r"^metal-(\d+)xl$", name)
        if metal_md:
            self._name = name
            self._size_value = int(metal_md[1])
            self._is_metal = True
            return
        xl_md = re.match(r"^(\d+)?xlarge$", name)
        if not xl_md:
            raise ValueError("Invalid size name")
        self._name = name
        self._is_metal = False
        if not xl_md[1]:
            self._size_value = 32
            return
        self._size_value = 32 * int(xl_md[1])

    def __str__(self: InstanceSize) -> str:
        """Get instance size name.

        Returns:
            str: Instance size name
        """
        return self._name

    def __eq__(self: InstanceSize, other: object) -> bool:
        """Whether instance size equals to other.

        Args:
            other: Other object

        Returns:
            bool: Whether this object equals to other
        """
        if not isinstance(other, InstanceSize):
            return False
        return self._name == other._name

    def __ne__(self: InstanceSize, other: object) -> bool:
        """Whether instance size does not equals to other.

        Args:
            other: Other object

        Returns:
            bool: Whether this object does not equals to other
        """
        return not (self == other)

    def __lt__(self: InstanceSize, other: object) -> bool:
        """Whether instance size is lesser than other.

        Args:
            other: Other object

        Returns:
            Whether instance size is lesser than other

        Raises:
            NotImplementedError: If not comparable
        """
        if isinstance(other, str):
            try:
                target = InstanceSize(other)
            except ValueError:
                raise NotImplementedError("Cannot compare with other")
        elif isinstance(other, InstanceSize):
            target = other
        else:
            raise NotImplementedError("Cannot compare with other")
        if self._is_metal and not target._is_metal:
            return False
        if not self._is_metal and target._is_metal:
            return True
        return self._size_value < target._size_value

    def __le__(self: InstanceSize, other: object) -> bool:
        """Whether instance size is lesser than or equals to other.

        Args:
            other: Other object

        Returns:
            Whether instance size is lesser than other

        Raises:
            NotImplementedError: If not comparable
        """
        if isinstance(other, str):
            try:
                target = InstanceSize(other)
            except ValueError:
                raise NotImplementedError("Cannot compare with other")
        elif isinstance(other, InstanceSize):
            target = other
        else:
            raise NotImplementedError("Cannot compare with other")
        if self._is_metal and not target._is_metal:
            return False
        if not self._is_metal and target._is_metal:
            return True
        return self._size_value <= target._size_value

    def __gt__(self: InstanceSize, other: object) -> bool:
        """Whether instance size is greater than other.

        Args:
            other: Other object

        Returns:
            Whether instance size is lesser than other

        Raises:
            NotImplementedError: If not comparable
        """
        if isinstance(other, str):
            try:
                target = InstanceSize(other)
            except ValueError:
                raise NotImplementedError("Cannot compare with other")
        elif isinstance(other, InstanceSize):
            target = other
        else:
            raise NotImplementedError("Cannot compare with other")
        if self._is_metal and not target._is_metal:
            return True
        if not self._is_metal and target._is_metal:
            return False
        return self._size_value > target._size_value

    def __ge__(self: InstanceSize, other: object) -> bool:
        """Whether instance size is greater than or equals to other.

        Args:
            other: Other object

        Returns:
            Whether instance size is lesser than or equals to other

        Raises:
            NotImplementedError: If not comparable
        """
        if isinstance(other, str):
            try:
                target = InstanceSize(other)
            except ValueError:
                raise NotImplementedError("Cannot compare with other")
        elif isinstance(other, InstanceSize):
            target = other
        else:
            raise NotImplementedError("Cannot compare with other")
        if self._is_metal and not target._is_metal:
            return True
        if not self._is_metal and target._is_metal:
            return False
        return self._size_value >= target._size_value


# Amazon FinSpace

# Amazon Redshift

# AWS AppSync cache

# Amazon Managed Blockchain

# AWS CodeBuild

# Amazon AppStream 2.0

# Amazon HealthOmics private workflow
