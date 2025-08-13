-- inserir alguns registros (Athena suporta INSERT em Iceberg)
INSERT INTO db_name.usuarios VALUES 
  (1,'Ana','ana@example.com', current_timestamp),
  (2,'Bruno','bruno@example.com', current_timestamp);

SELECT * FROM db_name.usuarios;

-- particionamento por hora (exemplo de evolução de esquema/layout)
ALTER TABLE db_name.usuarios
SET TBLPROPERTIES ('partitioning'='hour(created_at)');
