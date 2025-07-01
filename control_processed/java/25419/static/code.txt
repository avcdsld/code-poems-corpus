@Override
  public S handle(int version, water.api.Route route, Properties parms, String postBody) throws Exception {
    // Only here for train or validate-parms
    if( !route._handler_method.getName().equals("train") )
      throw water.H2O.unimpl();

    // Peek out the desired algo from the URL
    String ss[] = route._url.split("/");
    String algoURLName = ss[3]; // {}/{99}/{Grid}/{gbm}/
    String algoName = ModelBuilder.algoName(algoURLName); // gbm -> GBM; deeplearning -> DeepLearning
    String schemaDir = ModelBuilder.schemaDirectory(algoURLName);
    // Get the latest version of this algo: /99/Grid/gbm  ==> GBMV3
    // String algoSchemaName = SchemaServer.schemaClass(version, algoName).getSimpleName(); // GBMV3
    // int algoVersion = Integer.valueOf(algoSchemaName.substring(algoSchemaName.lastIndexOf("V")+1)); // '3'
    // Ok, i'm replacing one hack with another hack here, because SchemaServer.schema*() calls are getting eliminated.
    // There probably shouldn't be any reference to algoVersion here at all... TODO: unhack all of this
    int algoVersion = 3;
    if (algoName.equals("SVD") || algoName.equals("Aggregator") || algoName.equals("StackedEnsemble")) algoVersion = 99;

    // TODO: this is a horrible hack which is going to cause maintenance problems:
    String paramSchemaName = schemaDir+algoName+"V"+algoVersion+"$"+ModelBuilder.paramName(algoURLName)+"V"+algoVersion;

    // Build the Grid Search schema, and fill it from the parameters
    S gss = (S) new GridSearchSchema();
    gss.init_meta();
    gss.parameters = (P)TypeMap.newFreezable(paramSchemaName);
    gss.parameters.init_meta();
    gss.hyper_parameters = new IcedHashMap<>();

    // Get default parameters, then overlay the passed-in values
    ModelBuilder builder = ModelBuilder.make(algoURLName,null,null); // Default parameter settings
    gss.parameters.fillFromImpl(builder._parms); // Defaults for this builder into schema

    gss.fillFromParms(parms);   // Override defaults from user parms

    // Verify list of hyper parameters
    // Right now only names, no types
    // note: still use _validation_frame and and _training_frame at this point.
    // Do not change those names yet.
    validateHyperParams((P)gss.parameters, gss.hyper_parameters);

    // Get actual parameters
    MP params = (MP) gss.parameters.createAndFillImpl();

    Map<String,Object[]> sortedMap = new TreeMap<>(gss.hyper_parameters);

    // Need to change validation_frame to valid now.  HyperSpacewalker will complain
    // if it encountered an illegal parameter name.  From now on, validation_frame,
    // training_fame are no longer valid names.
    if (sortedMap.containsKey("validation_frame")) {
      sortedMap.put("valid", sortedMap.get("validation_frame"));
      sortedMap.remove("validation_frame");
    }

    // Get/create a grid for given frame
    // FIXME: Grid ID is not pass to grid search builder!
    Key<Grid> destKey = gss.grid_id != null ? gss.grid_id.key() : null;
    // Create target grid search object (keep it private for now)
    // Start grid search and return the schema back with job key
    Job<Grid> gsJob = GridSearch.startGridSearch(
        destKey,
        params,
        sortedMap,
        new DefaultModelParametersBuilderFactory<MP, P>(),
        (HyperSpaceSearchCriteria) gss.search_criteria.createAndFillImpl()
    );

    // Fill schema with job parameters
    // FIXME: right now we have to remove grid parameters which we sent back
    gss.hyper_parameters = null;
    gss.total_models = gsJob._result.get().getModelCount(); // TODO: looks like it's currently always 0
    gss.job = new JobV3(gsJob);

    return gss;
  }