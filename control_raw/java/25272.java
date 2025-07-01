@Override public S fillFromImpl(B builder) {
    // DO NOT, because it can already be running: builder.init(false); // check params

    this.algo = builder._parms.algoName().toLowerCase();
    this.algo_full_name = builder._parms.fullName();
    this.supervised = builder.isSupervised();

    this.can_build = builder.can_build();
    this.visibility = builder.builderVisibility();
    job = builder._job == null ? null : new JobV3(builder._job);
    // In general, you can ask about a builder in-progress, and the error
    // message list can be growing - so you have to be prepared to read it
    // racily.  Common for Grid searches exploring with broken parameter
    // choices.
    final ModelBuilder.ValidationMessage[] msgs = builder._messages; // Racily growing; read only once
    if( msgs != null ) {
      this.messages = new ValidationMessageV3[msgs.length];
      int i = 0;
      for (ModelBuilder.ValidationMessage vm : msgs) {
        if( vm != null ) this.messages[i++] = new ValidationMessageV3().fillFromImpl(vm); // TODO: version // Note: does default field_name mapping
      }
      // default fieldname hacks
      ValidationMessageV3.mapValidationMessageFieldNames(this.messages, new String[]{"_train", "_valid"}, new
          String[]{"training_frame", "validation_frame"});
    }
    this.error_count = builder.error_count();
    parameters = createParametersSchema();
    parameters.fillFromImpl(builder._parms);
    parameters.model_id = builder.dest() == null ? null : new KeyV3.ModelKeyV3(builder.dest());
    return (S)this;
  }