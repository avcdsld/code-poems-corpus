@Override
  protected void postGlobal() {
    assert(_res.model_info().get_params()._replicate_training_data);
    super.postGlobal();
    // model averaging (DeepWaterTask only computed the per-node models, each on all the data)
//    _res.model_info().div(_res._chunk_node_count);
    _res.model_info().add_processed_global(_res.model_info().get_processed_local()); //switch from local counters to global counters
    _res.model_info().set_processed_local(0L);
    _sharedmodel = _res.model_info();
  }