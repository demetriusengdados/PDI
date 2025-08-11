aws dms create-replication-instance \
    --replication-instance-identifier dms-instance-cliente \
    --replication-instance-class dms.t3.medium \
    --allocated-storage 100 \
    --vpc-security-group-ids sg-xxxxxxxx \
    --availability-zone us-east-1a \
    --tags Key=Project,Value=DataLake
