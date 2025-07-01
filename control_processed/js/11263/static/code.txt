function (state, payload) {
        var entity = payload.entity;
        var data = payload.data;
        var where = payload.where || null;
        var options = OptionsBuilder.createPersistOptions(payload);
        var result = payload.result;
        result.data = (new Query(state, entity)).update(data, where, options);
    }