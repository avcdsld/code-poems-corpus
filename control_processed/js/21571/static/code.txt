function runQuery(query, connection) {
  const pgConfig = {
    user: connection.username,
    password: connection.password,
    database: connection.database,
    host: connection.host,
    ssl: connection.postgresSsl,
    stream: createSocksConnection(connection)
  };
  // TODO cache key/cert values
  if (connection.postgresKey && connection.postgresCert) {
    pgConfig.ssl = {
      key: fs.readFileSync(connection.postgresKey),
      cert: fs.readFileSync(connection.postgresCert)
    };
    if (connection.postgresCA) {
      pgConfig.ssl['ca'] = fs.readFileSync(connection.postgresCA);
    }
  }
  if (connection.port) pgConfig.port = connection.port;

  return new Promise((resolve, reject) => {
    const client = new pg.Client(pgConfig);
    client.connect(err => {
      if (err) {
        client.end();
        return reject(err);
      }
      const cursor = client.query(new PgCursor(query));
      return cursor.read(connection.maxRows + 1, (err, rows) => {
        if (err) {
          // pg_cursor can't handle multi-statements at the moment
          // as a work around we'll retry the query the old way, but we lose the maxRows protection
          return client.query(query, (err, result) => {
            client.end();
            if (err) {
              return reject(err);
            }
            return resolve({ rows: result.rows });
          });
        }
        let incomplete = false;
        if (rows.length === connection.maxRows + 1) {
          incomplete = true;
          rows.pop(); // get rid of that extra record. we only get 1 more than the max to see if there would have been more...
        }
        if (err) {
          reject(err);
        } else {
          resolve({ rows, incomplete });
        }
        cursor.close(err => {
          if (err) {
            console.log('error closing pg-cursor:');
            console.log(err);
          }
          // Calling end() without setImmediate causes error within node-pg
          setImmediate(() => {
            client.end(error => {
              if (error) {
                console.error(error);
              }
            });
          });
        });
      });
    });
  });
}