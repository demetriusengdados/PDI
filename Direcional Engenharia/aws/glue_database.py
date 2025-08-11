import boto3

glue = boto3.client('glue')

response = glue.create_database(
    DatabaseInput={
        'Name': 'cliente_datalake',
        'Description': 'Catálogo de dados para ingestão e transformação',
    }
)
print("Glue Database criado com sucesso!")
