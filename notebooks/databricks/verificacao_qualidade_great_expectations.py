'''// Notebook 6 - Verificação de qualidade com Great Expectations'''
import great_expectations as ge

context = ge.get_context()
df = spark.read.format("delta").load("/mnt/silver/produtos")

dataset = ge.dataset.SparkDFDataset(df)
dataset.expect_column_values_to_not_be_null("produto_id")
dataset.expect_column_values_to_be_between("preco", min_value=1, max_value=10000)

results = dataset.validate()
print(results)