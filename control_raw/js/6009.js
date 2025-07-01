function extendFromRecommended(config) {
    const newConfig = Object.assign({}, config);

    ConfigOps.normalizeToStrings(newConfig);

    const recRules = Object.keys(recConfig.rules).filter(ruleId => ConfigOps.isErrorSeverity(recConfig.rules[ruleId]));

    recRules.forEach(ruleId => {
        if (lodash.isEqual(recConfig.rules[ruleId], newConfig.rules[ruleId])) {
            delete newConfig.rules[ruleId];
        }
    });
    newConfig.extends = RECOMMENDED_CONFIG_NAME;
    return newConfig;
}