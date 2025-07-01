function step1c(token) {
    var categorizedGroups = categorizeGroups(token);

    if(token.substr(-1) == 'y' && categorizedGroups.substr(0, categorizedGroups.length - 1).indexOf('V') > -1) {
        return token.replace(/y$/, 'i');
    }

    return token;
}