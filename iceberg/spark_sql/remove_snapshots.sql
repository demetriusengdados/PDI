CALL glue_catalog.system.expire_snapshots(
  table => 'db_name.usuarios',
  older_than => TIMESTAMP '2025-01-01 00:00:00',
  retain_last => 5
);
-- Remove snapshots older than a specific date and keep the last 5 snapshots
CALL glue_catalog.system.remove_snapshots(  
  table => 'db_name.usuarios',
  older_than => TIMESTAMP '2025-01-01 00:00:00',
  retain_last => 5
);