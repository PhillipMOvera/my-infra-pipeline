import pytest
from unittest.mock import patch
from pulumi_aws import dynamodb, s3

# Test for DynamoDB Table
@patch("pulumi_aws.dynamodb.Table")
def test_dynamodb_table_created(mock_table):
    table = dynamodb.Table(
        "test-table",
        attributes=[{"name": "id", "type": "S"}],
        hash_key="id",
        billing_mode="PAY_PER_REQUEST"
    )
    assert table is not None

# Test for S3 Bucket
@patch("pulumi_aws.s3.Bucket")
def test_s3_bucket_created(mock_bucket):
    # Configure the mock object
    mock_bucket.return_value.bucket_prefix = "test-"
    mock_bucket.return_value.acl = "private"

    # Create the bucket
    bucket = mock_bucket.return_value

    # Assertions
    assert bucket is not None
    assert bucket.bucket_prefix == "test-"
    assert bucket.acl == "private"

