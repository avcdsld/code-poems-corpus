function resolveAddresses(provider, value, paramType) {
    if (Array.isArray(paramType)) {
        var promises_1 = [];
        paramType.forEach(function (paramType, index) {
            var v = null;
            if (Array.isArray(value)) {
                v = value[index];
            }
            else {
                v = value[paramType.name];
            }
            promises_1.push(resolveAddresses(provider, v, paramType));
        });
        return Promise.all(promises_1);
    }
    if (paramType.type === 'address') {
        return provider.resolveName(value);
    }
    if (paramType.type === 'tuple') {
        return resolveAddresses(provider, value, paramType.components);
    }
    // Strips one level of array indexing off the end to recuse into
    var isArrayMatch = paramType.type.match(/(.*)(\[[0-9]*\]$)/);
    if (isArrayMatch) {
        if (!Array.isArray(value)) {
            throw new Error('invalid value for array');
        }
        var promises = [];
        var subParamType = {
            components: paramType.components,
            type: isArrayMatch[1],
        };
        value.forEach(function (v) {
            promises.push(resolveAddresses(provider, v, subParamType));
        });
        return Promise.all(promises);
    }
    return Promise.resolve(value);
}