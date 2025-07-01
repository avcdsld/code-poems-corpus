public static HttpLogFilter defaultFilter() {
    return new HttpLogFilter() { // this is much prettier with 1.8 lambdas
      @Override public LogFilterLevel filter(RequestUri uri, Properties header, Properties parms) {
        // static web content
        String url = uri.getUrl();
        if (url.endsWith(".css") ||
            url.endsWith(".js")  || 
            url.endsWith(".png") || 
            url.endsWith(".ico")
        ) {
          return LogFilterLevel.DO_NOT_LOG;
        }
        // endpoints that might take sensitive parameters (passwords and other credentials)
        String[] path = uri.getPath();
        if (path[2].equals("PersistS3") ||
            path[2].equals("ImportSQLTable") ||
            path[2].equals("DecryptionSetup")
        ) {
          return LogFilterLevel.URL_ONLY;
        }
        // endpoints that are called very frequently AND DON'T accept any sensitive information in parameters
        if (path[2].equals("Cloud") ||
            path[2].equals("Jobs") && uri.isGetMethod() ||
            path[2].equals("Log") ||
            path[2].equals("Progress") ||
            path[2].equals("Typeahead") ||
            path[2].equals("WaterMeterCpuTicks")
        ) {
          return LogFilterLevel.DO_NOT_LOG;
        }
        return LogFilterLevel.LOG;
      }
    };
  }