-- macros/format_date.sql

{% macro format_date(col) %}
    date_trunc('day', {{ col }})
{% endmacro %}

{{ format_date("data_transacao") }}
{{ format_date("data_venda") }}
{{ format_date("data_pagamento") }}
{{ format_date("data_nascimento") }}
{{ format_date("data_entrada") }}
{{ format_date("data_saida") }}
{{ format_date("data_fim") }}
{{ format_date("data_inicio") }}
{{ format_date("data_geracao") }}
{{ format_date("data_atualizacao") }}
{{ format_date("data_validade") }}
{{ format_date("data_referencia") }}
{{ format_date("data_ultimo_pagamento") }}
{{ format_date("data_primeiro_pagamento") }}
{{ format_date("data_ultimo_acesso") }}
{{ format_date("data_primeiro_acesso") }}
{{ format_date("data_ultimo_login") }}
{{ format_date("data_primeiro_login") }}
{{ format_date("data_ultimo_envio") }}
{{ format_date("data_primeiro_envio") }}
{{ format_date("data_ultimo_download") }}
{{ format_date("data_primeiro_download") }}
{{ format_date("data_ultimo_acesso_api") }}
{{ format_date("data_primeiro_acesso_api") }}
{{ format_date("data_ultimo_acesso_sistema") }}
{{ format_date("data_primeiro_acesso_sistema") }}
{{ format_date("data_ultimo_acesso_app") }}
{{ format_date("data_primeiro_acesso_app") }}
{{ format_date("data_ultimo_acesso_web") }}
{{ format_date("data_primeiro_acesso_web") }}
{{ format_date("data_ultimo_acesso_email") }}
{{ format_date("data_primeiro_acesso_email") }}
{{ format_date("data_ultimo_acesso_sms") }}
{{ format_date("data_primeiro_acesso_sms") }}
{{ format_date("data_ultimo_acesso_push") }}
{{ format_date("data_primeiro_acesso_push") }}