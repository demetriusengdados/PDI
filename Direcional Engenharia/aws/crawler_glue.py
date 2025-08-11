response = glue.create_crawler(
    Name='crawler_raw_zone',
    Role='arn:aws:iam::123456789012:role/AWSGlueServiceRole',
    DatabaseName='cliente_datalake',
    Targets={
        'S3Targets': [{'Path': 's3://cliente-datalake-raw/'}],
    },
    TablePrefix='raw_',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
    }
)
glue.start_crawler(Name='crawler_raw_zone')
