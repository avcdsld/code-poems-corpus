TwoDimTable createSummaryTable() {
    TwoDimTable table = new TwoDimTable(
        "Status of Deep Learning Model",
        (get_params()._network == null ? ("MLP: " + Arrays.toString(get_params()._hidden)) : get_params()._network.toString()) + ", " + PrettyPrint.bytes(size()) + ", "
        + (!get_params()._autoencoder ? ("predicting " + get_params()._response_column + ", ") : "") +
            (get_params()._autoencoder ? "auto-encoder" :
                _classification ? (_classes + "-class classification") : "regression")
            + ", "
            + String.format("%,d", get_processed_global()) + " training samples, "
            + "mini-batch size " + String.format("%,d", get_params()._mini_batch_size),
        new String[1], //rows
        new String[]{"Input Neurons", "Rate", "Momentum" },
        new String[]{"int", "double", "double" },
        new String[]{"%d", "%5f", "%5f"},
        "");
    table.set(0, 0, _dataInfo!=null ? _dataInfo.fullN() : _width * _height * _channels);
    table.set(0, 1, get_params().learningRate(get_processed_global()));
    table.set(0, 2, get_params().momentum(get_processed_global()));
    summaryTable = table;
    return summaryTable;
  }