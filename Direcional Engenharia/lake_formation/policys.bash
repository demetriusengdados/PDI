aws lakeformation grant-permissions \
  --principal '{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:user/analista-marketing"}' \
  --resource '{
    "TableWithColumns": {
      "DatabaseName": "cliente_datalake",
      "Name": "raw_clientes",
      "ColumnWildcard": {
        "ExcludedColumnNames": ["cpf", "email"]
      }
    }
  }' \
  --permissions "SELECT"
    --permissions-with-grant-option "SELECT" \
    --region us-east-1 \
    --profile direcional-engenharia \
  --output json \
  --no-cli-pager
  --debug
  --no-verify-ssl
  --cli-input-json file://path/to/input.json \
  --generate-cli-skeleton
    --no-paginate \
    --max-items 100 \
    --starting
    --page-size 10 \
    --query 'GrantResponse' \
    --no-color \
    --no-sign-request \
    --endpoint-url https://lakeformation.us-east-1.amazonaws.com \
    --cli-read-timeout 60 \
    --cli-connect-timeout 30 \
    --no-include-email \
    --no-include-credentials \
    --no-include-headers \
    --no-include-body \
    --no-include-params \
    --no-include-aws-request \
    --no-include-aws-response \
    --no-include-aws-signature \
    --no-include-aws-request-id \
    --no-include-aws-region \
    --no-include-aws-service \
    --no-include-aws-operation \
    --no-include-aws-version \
    --no-include-aws-cli \
    --no-include-aws-cli-version \
    --no-include-aws-cli-command \
    --no-include-aws-cli-args \
    --no-include-aws-cli-output \
    --no-include-aws-cli-profile \
    --no-include-aws-cli-region \
    --no-include-aws-cli-output-format \
    --no-include-aws-cli-pager \
    --no-include-aws-cli-debug \
    --no-include-aws-cli-verify-ssl \
    --no-include-aws-cli-cli-input-json \
    --no-include-aws-cli-generate-cli-skeleton \
    --no-include-aws-cli-paginate \
    --no-include-aws-cli-max-items \
    --no-include-aws-cli-starting-token \
    --no-include-aws-cli-page-size \
    --no-include-aws-cli-query \
    --no-include-aws-cli-color \
    --no-include-aws-cli-sign-request \
    --no-include-aws-cli-endpoint-url \
    --no-include-aws-cli-cli-read-timeout\
    --no-include-aws-cli-cli-connect-timeout \
    --no-include-aws-cli-no-include-email \
    --no-include-aws-cli-no-include-credentials \
aws lakeformation put-data-lake-settings \
  --data-lake-settings '{
    "DataLakeAdmins": [{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/Admin"}],
    "CreateDatabaseDefaultPermissions": [],
    "CreateTableDefaultPermissions": []
  }'
    --cli-input-json file://path/to/data-lake-settings.json \
    --generate-cli-skeleton \
    --region us-east-1 \
    --profile direcional-engenharia \
  --output json \
  --no-cli-pager \
    --debug \
    --no-verify-ssl \
    --no-paginate \ 
    --max-items 100 \
    --starting-token "" \
    --page-size 10 \
    --query 'DataLakeSettings' \
    --no-color \
    --no-sign-request \
    --endpoint-url https://lakeformation.us-east-1.amazonaws.com \