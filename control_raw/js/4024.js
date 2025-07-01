function setResults(fullpath, resultInfo, maxResultsToReturn) {
    if (results[fullpath]) {
        numMatches -= results[fullpath].matches.length;
        delete results[fullpath];
    }

    if (foundMaximum || !resultInfo || !resultInfo.matches || !resultInfo.matches.length) {
        return;
    }

    // Make sure that the optional `collapsed` property is explicitly set to either true or false,
    // to avoid logic issues later with comparing values.
    resultInfo.collapsed = collapseResults;

    results[fullpath] = resultInfo;
    numMatches += resultInfo.matches.length;
    evaluatedMatches += resultInfo.matches.length;
    maxResultsToReturn = maxResultsToReturn || MAX_RESULTS_TO_RETURN;
    if (numMatches >= maxResultsToReturn || evaluatedMatches > MAX_TOTAL_RESULTS) {
        foundMaximum = true;
    }
}