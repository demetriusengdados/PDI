aws lakeformation add-lf-tags-to-resource \
  --resource '{"Table":{"DatabaseName":"cliente_datalake","Name":"raw_clientes"}}' \
  --lf-tags '[{"Key":"Sensibilidade","Value":"Alto"}]'
aws lakeformation add-lf-tags-to-resource \
  --resource '{"Table":{"DatabaseName":"cliente_datalake","Name":"raw_fornecedores"}}' \
  --lf-tags '[{"Key":"Sensibilidade","Value":"Alto"}]'
aws lakeformation add-lf-tags-to-resource \
  --resource '{"Table":{"DatabaseName":"cliente_datalake","Name":"raw_vendas"}}' \
  --lf-tags '[{"Key":"Sensibilidade","Value":"Alto"}]'
aws lakeformation add-lf-tags-to-resource \
  --resource '{"Table":{"DatabaseName":"cliente_datalake","Name":"raw_produtos"}}' \