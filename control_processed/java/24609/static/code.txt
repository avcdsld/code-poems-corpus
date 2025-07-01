private static void populateHiveConf(HiveConf hiveConf, String[] args) {

    if (args == null) {
      return;
    }

    int index = 0;
    for (; index < args.length; index++) {
      if ("-hiveconf".equals(args[index])) {
        String hiveConfParam = stripSingleDoubleQuote(args[++index]);

        String[] tokens = hiveConfParam.split("=");
        if (tokens.length == 2) {
          String name = tokens[0];
          String value = tokens[1];
          logger.info("Setting: " + name + "=" + value + " to hiveConf");
          hiveConf.set(name, value);
        } else {
          logger.warn("Invalid hiveconf: " + hiveConfParam);
        }
      }
    }
  }