public Frame toFrame() {
    Vec zeroVec = null;
    try {
      zeroVec = Vec.makeZero(_output._words.length);
      byte[] types = new byte[1 + _output._vecSize];
      Arrays.fill(types, Vec.T_NUM);
      types[0] = Vec.T_STR;
      String[] colNames = new String[types.length];
      colNames[0] = "Word";
      for (int i = 1; i < colNames.length; i++)
        colNames[i] = "V" + i;
      return new ConvertToFrameTask(this).doAll(types, zeroVec).outputFrame(colNames, null);
    } finally {
      if (zeroVec != null) zeroVec.remove();
    }
  }