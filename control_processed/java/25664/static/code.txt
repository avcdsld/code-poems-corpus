@SuppressWarnings("unused") // called through reflection by RequestServer
  public ModelBuildersV3 list(int version, ModelBuildersV3 m) {
    m.model_builders = new ModelBuilderSchema.IcedHashMapStringModelBuilderSchema();
    for( String algo : ModelBuilder.algos() ) {
      ModelBuilder builder = ModelBuilder.make(algo, null, null);
      m.model_builders.put(algo.toLowerCase(), (ModelBuilderSchema)SchemaServer.schema(version, builder).fillFromImpl(builder));
    }
    return m;
  }