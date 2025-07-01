@Override
  public ParseSetup createParserSetup(Key[] inputs, ParseSetup requiredSetup) {

    FileVec f;
    Object frameOrVec = DKV.getGet(inputs[0]);

    if (frameOrVec instanceof water.fvec.Frame)
      f = (FileVec) ((Frame) frameOrVec).vec(0);
    else
      f = (FileVec) frameOrVec;
    return readSetup(f, requiredSetup.getColumnNames(), requiredSetup.getColumnTypes());
  }