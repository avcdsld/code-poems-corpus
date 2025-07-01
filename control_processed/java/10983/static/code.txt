public SearchResult getSuggestions(StaplerRequest req, String query) {
        Set<String> paths = new HashSet<>();  // paths already added, to control duplicates
        SearchResultImpl r = new SearchResultImpl();
        int max = req.hasParameter("max") ? Integer.parseInt(req.getParameter("max")) : 100;
        SearchableModelObject smo = findClosestSearchableModelObject(req);
        for (SuggestedItem i : suggest(makeSuggestIndex(req), query, smo)) {
            if(r.size()>=max) {
                r.hasMoreResults = true;
                break;
            }
            if(paths.add(i.getPath()))
                r.add(i);
        }
        return r;
    }