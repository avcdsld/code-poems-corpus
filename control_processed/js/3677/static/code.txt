function (id, context) {
            var scopeCounter;

            context = this._getContext(context);

            var scopeOrder = this._getScopeOrder(context);

            for (scopeCounter = 0; scopeCounter < scopeOrder.length; scopeCounter++) {
                var scope = this._scopes[scopeOrder[scopeCounter]];
                if (scope) {
                    var result = scope.get(id, context);
                    if (result !== undefined) {
                        var pref      = this.getPreference(id),
                            validator = pref && pref.validator;
                        if (!validator || validator(result)) {
                            if (pref && pref.type === "object") {
                                result = _.extend({}, pref.initial, result);
                            }
                            return _.cloneDeep(result);
                        }
                    }
                }
            }
        }