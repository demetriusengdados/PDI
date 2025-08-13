aws glue create-database --database-input '{
  "Name": "db_name",
  "Description": "Iceberg demo",
  "LocationUri": "s3://my-iceberg-lake/iceberg/db_name/"
}'
