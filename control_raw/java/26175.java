public SearchResult<WorkflowSummary> search(Integer start, Integer size, String sort, String freeText, String query) {
        Object[] params = new Object[]{"start", start, "size", size, "sort", sort, "freeText", freeText, "query", query};
        return getForEntity("workflow/search", params, searchResultWorkflowSummary);
    }