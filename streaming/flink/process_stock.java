DataStream<String> stream = env
    .addSource(new FlinkKafkaConsumer<>("estoque.produtos", new SimpleStringSchema(), props));

stream.map(json -> parseProduct(json))
      .addSink(new IcebergSink(...));
