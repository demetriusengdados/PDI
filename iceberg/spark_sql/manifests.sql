CALL glue_catalog.system.rewrite_manifests('db_name.usuarios');
-- Rewrites the manifests for the specified table
CALL glue_catalog.system.rewrite_data_files('db_name.usuarios');

