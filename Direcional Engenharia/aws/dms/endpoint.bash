aws dms create-endpoint \
  --endpoint-identifier oracle-onprem \
  --endpoint-type source \
  --engine-name oracle \
  --username YOUR_DB_USER \
  --password YOUR_DB_PASSWORD \
  --server-name YOUR_ORACLE_HOST \
  --port 1521 \
  --database-name YOUR_DB_NAME \
  --extra-connection-attributes "useLogminerReader=N;useBfile=Y;" \
  --tags Key=Environment,Value=Dev


aws dms create-endpoint \
  --endpoint-identifier s3-raw-datalake \
  --endpoint-type target \
  --engine-name s3 \
  --s3-settings BucketName=cliente-datalake-raw,BucketFolder=oracle_dump,CompressionType=GZIP \
  --service-access-role-arn arn:aws:iam::123456789012:role/dms-s3-access-role
aws dms create-endpoint \
  --endpoint-identifier s3-staging-datalake \