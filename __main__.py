import pulumi
import pulumi_aws as aws

# Create an S3 bucket
bucket = aws.s3.Bucket("my-pulumi-bucket", bucket_prefix="pulumi-demo-", acl="private")

# Export the bucket name
pulumi.export("bucket_name", bucket.id)

# Create a DynamoDB table
table = aws.dynamodb.Table(
    "my-dynamodb-table",
    attributes=[
        {"name": "id", "type": "S"}  # Define a string attribute named 'id'
    ],
    hash_key="id",  # Define 'id' as the hash key
    billing_mode="PAY_PER_REQUEST"  # Use on-demand pricing
)

# Export the DynamoDB table name
pulumi.export("dynamodb_table_name", table.name)