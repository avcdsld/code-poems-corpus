function (table, key, obj, clientIdentity) {
            // Create table if it doesnt exist:
            db.tables[table] = db.tables[table] || {};
            // Put the obj into to table
            db.tables[table][key] = obj;
            // Register the change:
            db.changes.push({
                rev: ++db.revision,
                source: clientIdentity,
                type: CREATE,
                table: table,
                key: key,
                obj: obj
            });
            db.trigger();
        }