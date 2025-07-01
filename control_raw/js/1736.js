function findAll(unfilteredOptions) {
        var options = this.filterOptions(unfilteredOptions, 'findAll'),
            itemCollection = this.forge();

        // @TODO: we can't use order raw when running migrations (see https://github.com/tgriesser/knex/issues/2763)
        if (this.orderDefaultRaw && !options.migrating) {
            itemCollection.query((qb) => {
                qb.orderByRaw(this.orderDefaultRaw(options));
            });
        }

        itemCollection.applyDefaultAndCustomFilters(options);
        return itemCollection.fetchAll(options).then(function then(result) {
            if (options.withRelated) {
                _.each(result.models, function each(item) {
                    item.withRelated = options.withRelated;
                });
            }

            return result;
        });
    }