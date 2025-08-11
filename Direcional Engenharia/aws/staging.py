import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Lê dados da raw zone
raw_df = glueContext.create_dynamic_frame.from_catalog(
    database="cliente_datalake",
    table_name="raw_clientes",
    transformation_ctx="raw_df"
)

# Transformações simples (exemplo: limpeza de nulos)
staged_df = raw_df.drop_null_fields()

# Grava na staging zone
glueContext.write_dynamic_frame.from_options(
    frame=staged_df,
    connection_type="s3",
    connection_options={"path": "s3://cliente-datalake-staging/clientes/"},
    format="parquet"
)

job.commit()
