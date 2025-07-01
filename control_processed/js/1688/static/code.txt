function doQuery(options) {
            return models.User.transferOwnership(options.data.owner[0], _.omit(options, ['data']))
                .then((models) => {
                    return {
                        users: models.toJSON(_.omit(options, ['data']))
                    };
                });
        }