@Override public Word2VecModel createImpl() {
    Word2VecModel.Word2VecParameters parms = parameters.createImpl();
    return new Word2VecModel( model_id.key(), parms, null);
  }