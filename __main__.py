import pulumi
import pulumi_aws as aws

# Create an S3 bucket
bucket = aws.s3.Bucket("my-pulumi-bucket", bucket_prefix="pulumi-demo-", acl="private")

# Export the bucket name
pulumi.export("bucket_name", bucket.id)
