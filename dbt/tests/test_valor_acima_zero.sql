-- tests/test_valor_acima_zero.sql

select *
from {{ ref('fct_transacoes') }}
where valor < 0
    and {{ test_valor_acima_zero('valor') }} = 0
    and {{ test_valor_acima_zero('valor') }} is not null
    and {{ test_valor_acima_zero('valor') }} is not false
    and {{ test_valor_acima_zero('valor') }} is not true
    and {{ test_valor_acima_zero('valor') }} is not empty
    and {{ test_valor_acima_zero('valor') }} is not blank
    and {{ test_valor_acima_zero('valor') }} is not zero
    and {{ test_valor_acima_zero('valor') }} is not negative