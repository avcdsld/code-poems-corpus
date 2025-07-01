function (oldContext, newContext) {
            var changes = [],
                data    = this.data;

            _.each(this._layers, function (layer) {
                if (data[layer.key] && oldContext[layer.key] !== newContext[layer.key]) {
                    var changesInLayer = layer.contextChanged(data[layer.key],
                                                              oldContext,
                                                              newContext);
                    if (changesInLayer) {
                        changes.push(changesInLayer);
                    }
                }
            });
            return _.union.apply(null, changes);
        }