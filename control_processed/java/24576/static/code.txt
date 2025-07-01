public static AzkabanDataSource getDataSource(final Props props) {
    final String databaseType = props.getString("database.type");

    AzkabanDataSource dataSource = null;
    if (databaseType.equals("mysql")) {
      final int port = props.getInt("mysql.port");
      final String host = props.getString("mysql.host");
      final String database = props.getString("mysql.database");
      final String user = props.getString("mysql.user");
      final String password = props.getString("mysql.password");
      final int numConnections = props.getInt("mysql.numconnections");

      dataSource =
          getMySQLDataSource(host, port, database, user, password,
              numConnections);
    } else if (databaseType.equals("h2")) {
      final String path = props.getString("h2.path");
      final Path h2DbPath = Paths.get(path).toAbsolutePath();
      logger.info("h2 DB path: " + h2DbPath);
      dataSource = getH2DataSource(h2DbPath);
    }

    return dataSource;
  }