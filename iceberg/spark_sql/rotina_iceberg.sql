-- otimiza dados pequenos (bin pack)
CALL glue_catalog.system.rewrite_data_files(table => 'db_name.usuarios', options => map('min-input-files','5'));
-- compacta arquivos pequenos
CALL glue_catalog.system.compact(table => 'db_name.usuarios', options => map('min-input-files','5'));