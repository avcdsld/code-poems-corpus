function validateRules(rulesConfig, ruleMapper, source = null) {
    if (!rulesConfig) {
        return;
    }

    Object.keys(rulesConfig).forEach(id => {
        validateRuleOptions(ruleMapper(id), id, rulesConfig[id], source);
    });
}