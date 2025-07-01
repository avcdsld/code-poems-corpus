function listFilters(plugins) {
    return plugins
        .reverse()
        .reduce(function(result, plugin) {
            return result.merge(plugin.getFilters());
        }, Immutable.Map());
}