-- models/marts/fct_transacoes.sql

with base as (
    select * from {{ ref('stg_transacoes') }}
)

select
    id_transacao,
    id_cliente,
    id_pedido,
    valor,
    moeda,
    status,
    forma_pagamento,
    data_transacao,
    bandeira_cartao,
    coalesce(parcelas, 1) as parcelas,
    {{ format_date("data_transacao") }} as data_transacao_formatada
from base
