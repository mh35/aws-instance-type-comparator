"""Instance type classes definition."""
from __future__ import annotations

from enum import Enum


class InstanceService(str, Enum):
    """Service for instance type."""

    EC2 = "ec2"
    CLOUDSEARCH = "cloudsearch"
    OPENSEARCH = "opensearch"
    KAFKA = "kafka"
