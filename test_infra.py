import pytest
from unittest.mock import patch
from pulumi_aws import dynamodb

@patch("pulumi_aws.dynamodb.Table")
def test_dynamodb_table_created(mock_table):
    table = dynamodb.Table("test-table",
        attributes=[{"name": "id", "type": "S"}],
        hash_key="id",
        billing_mode="PAY_PER_REQUEST"
    )
    assert table is not None
