public void setFilters(String filters)
    {
        for (String filter : filters.split(",")) {
            filteredFrames.add("at " + filter.trim());
        }
    }