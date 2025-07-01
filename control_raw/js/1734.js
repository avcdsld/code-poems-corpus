function sanitizeData(data) {
        var tableName = _.result(this.prototype, 'tableName'), date;

        _.each(data, (value, property) => {
            if (value !== null
                && schema.tables[tableName].hasOwnProperty(property)
                && schema.tables[tableName][property].type === 'dateTime'
                && typeof value === 'string'
            ) {
                date = new Date(value);

                // CASE: client sends `0000-00-00 00:00:00`
                if (isNaN(date)) {
                    throw new common.errors.ValidationError({
                        message: common.i18n.t('errors.models.base.invalidDate', {key: property}),
                        code: 'DATE_INVALID'
                    });
                }

                data[property] = moment(value).toDate();
            }

            if (this.prototype.relationships && this.prototype.relationships.indexOf(property) !== -1) {
                _.each(data[property], (relation, indexInArr) => {
                    _.each(relation, (value, relationProperty) => {
                        if (value !== null
                            && schema.tables[this.prototype.relationshipBelongsTo[property]].hasOwnProperty(relationProperty)
                            && schema.tables[this.prototype.relationshipBelongsTo[property]][relationProperty].type === 'dateTime'
                            && typeof value === 'string'
                        ) {
                            date = new Date(value);

                            // CASE: client sends `0000-00-00 00:00:00`
                            if (isNaN(date)) {
                                throw new common.errors.ValidationError({
                                    message: common.i18n.t('errors.models.base.invalidDate', {key: relationProperty}),
                                    code: 'DATE_INVALID'
                                });
                            }

                            data[property][indexInArr][relationProperty] = moment(value).toDate();
                        }
                    });
                });
            }
        });

        return data;
    }