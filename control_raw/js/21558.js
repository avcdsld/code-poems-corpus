function runQuery(query, connection) {
  const incomplete = false;

  return new Promise((resolve, reject) => {
    const client = hdb.createClient({
      host: connection.host,
      port: connection.hanaport,
      database: connection.hanadatabase,
      user: connection.username,
      password: connection.password,
      schema: connection.hanaSchema
    });

    client.on('error', err => {
      console.error('Network connection error', err);
      return reject(err);
    });

    client.connect(err => {
      if (err) {
        console.error('Connect error', err);
        return reject(err);
      }
      return client.execute(query, function(err, rs) {
        let rows = [];

        if (err) {
          client.disconnect();
          return reject(err);
        }

        if (!rs) {
          client.disconnect();
          return resolve({ rows, incomplete });
        }

        if (!rs.createObjectStream) {
          // Could be row count or something
          client.disconnect();
          return resolve({ rows: [{ result: rs }], incomplete });
        }

        const stream = rs.createObjectStream();

        stream.on('data', data => {
          if (rows.length < connection.maxRows) {
            return rows.push(data);
          }
          client.disconnect();
          return resolve({ rows, incomplete: true });
        });

        stream.on('error', error => {
          client.disconnect();
          return reject(error);
        });

        stream.on('finish', () => {
          client.disconnect();
          return resolve({ rows, incomplete });
        });
      });
    });
  });
}