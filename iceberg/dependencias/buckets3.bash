BUCKET=my-iceberg-lake
REGION=us-east-1
aws s3api create-bucket --bucket $BUCKET --region $REGION --create-bucket-configuration LocationConstraint=$REGION

# bloquear acesso público
aws s3api put-public-access-block --bucket $BUCKET --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

# versionamento
aws s3api put-bucket-versioning --bucket $BUCKET --versioning-configuration Status=Enabled

# criptografia padrão (SSE-S3 ou KMS)
aws s3api put-bucket-encryption --bucket $BUCKET --server-side-encryption-configuration '{
  "Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]
}'
