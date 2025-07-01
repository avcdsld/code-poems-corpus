function getProvidersForLanguageId(languageId) {
        var result = [];
        if (_providers[languageId]) {
            result = result.concat(_providers[languageId]);
        }
        if (_providers['*']) {
            result = result.concat(_providers['*']);
        }
        return result;
    }