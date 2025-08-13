CREATE TABLE db_name.usuarios (
  id          bigint,
  nome        string,
  email       string,
  created_at  timestamp
)
LOCATION 's3://my-iceberg-lake/iceberg/db_name/usuarios'
TBLPROPERTIES (
  'table_type'='ICEBERG',
  'format'='parquet',
  'write.parquet.compression-codec'='snappy',
  'commit.manifest.min.count.to.merge'='5',
  'engine.hive.enabled'='true' -- compat Glue
);
