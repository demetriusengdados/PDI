CREATE TABLE spark_catalog.db_name.iceberg_table (
  id BIGINT,
  nome STRING,
  email STRING,
  telefone STRING,
  cpf STRING,
  data_nascimento DATE,
  data_criacao DATE,
  ativo BOOLEAN,
  saldo DECIMAL(12,2),
  tipo_usuario STRING,
  endereco STRUCT<
    rua: STRING,
    numero: INT,
    cidade: STRING,
    estado: STRING,
    cep: STRING
  >
)
USING iceberg;
OPTIONS (
  'format-version' '2',
  'write.format.default' 'parquet',
  'location' 'hdfs://localhost:9000/user/hive/warehouse/db_name.db/iceberg_table'
);