import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Args
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura da staging zone (Glue Catalog)
staging_df = glueContext.create_dynamic_frame.from_catalog(
    database="cliente_datalake",
    table_name="staging_clientes",
    transformation_ctx="staging_df"
)

# Exemplo de transformação (padronização de nome)
transformed_df = staging_df.apply_mapping([
    ("id", "int", "id", "int"),
    ("nome", "string", "nome", "string"),
    ("email", "string", "email", "string"),
    ("data_cadastro", "string", "data_cadastro", "timestamp")
])

# Escrita no Redshift
glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=transformed_df,
    catalog_connection="redshift-conn",
    connection_options={
        "dbtable": "analytics.clientes_curados",
        "database": "datalake_dw"
    },
    redshift_tmp_dir="s3://cliente-datalake-temp/redshift/",
    transformation_ctx="redshift_writer"
)

job.commit()
