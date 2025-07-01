function runQuery(query, connection) {
  const params = {
    host: connection.host,
    port: connection.port ? connection.port : 5433,
    user: connection.username,
    password: connection.password,
    database: connection.database
  };

  return new Promise((resolve, reject) => {
    const client = vertica.connect(params, function(err) {
      if (err) {
        client.disconnect();
        return reject(err);
      }

      let incomplete = false;
      const rows = [];
      let finished = false;
      let columnNames = [];

      const verticaQuery = client.query(query);

      verticaQuery.on('fields', fields => {
        columnNames = fields.map(field => field.name);
      });

      verticaQuery.on('row', function(row) {
        if (rows.length < connection.maxRows) {
          const resultRow = {};
          row.forEach((value, index) => {
            resultRow[columnNames[index]] = value;
          });
          return rows.push(resultRow);
        }
        if (!finished) {
          finished = true;
          client.disconnect();
          incomplete = true;
          return resolve({ rows, incomplete });
        }
      });

      verticaQuery.on('end', function() {
        if (!finished) {
          finished = true;
          client.disconnect();
          return resolve({ rows, incomplete });
        }
      });

      verticaQuery.on('error', function(err) {
        if (!finished) {
          finished = true;
          client.disconnect();
          return reject(err);
        }
      });
    });
  });
}