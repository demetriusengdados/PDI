-- models/staging/stg_transacoes.sql

with source as (
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
        parcelas
    from {{ source('raw', 'transacoes') }}
)

select * from source
