"""Instance type classes definition."""
from __future__ import annotations

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


# Amazon FinSpace

# Amazon Redshift

# AWS AppSync cache

# Amazon Managed Blockchain

# AWS CodeBuild

# Amazon AppStream 2.0

# Amazon HealthOmics private workflow
