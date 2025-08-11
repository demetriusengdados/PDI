aws dms create-replication-task \
  --replication-task-identifier oracle-to-s3-task \
  --source-endpoint-arn arn:aws:dms:REGION:ACCOUNT:endpoint:oracle-onprem \
  --target-endpoint-arn arn:aws:dms:REGION:ACCOUNT:endpoint:s3-raw-datalake \
  --replication-instance-arn arn:aws:dms:REGION:ACCOUNT:rep:your-replication-instance \
  --migration-type full-load-and-cdc \
  --table-mappings file://mapping.json \
  --replication-task-settings file://task-settings.json
    --endpoint-type target \