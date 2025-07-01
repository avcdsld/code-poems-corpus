public SelectStatement mergeSubqueryStatement() {
        SelectStatement result = processLimitForSubquery();
        processItems(result);
        processOrderByItems(result);
        result.setParametersIndex(getParametersIndex());
        return result;
    }