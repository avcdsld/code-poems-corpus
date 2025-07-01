function (query, results) {
        // Filter components out of the results.
        return YArray.filter(results, function (result) {
            return result.raw.resultType === 'component' ? false : result;
        });
    }