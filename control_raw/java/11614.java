protected boolean isValidQuery(String query) {
        if (query == null) {
            return true;
        }
        
        return QUERY_PATTERN.matcher(query).matches();
    }