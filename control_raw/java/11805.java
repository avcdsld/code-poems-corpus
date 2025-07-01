@CheckForNull
    public UpdateSite getById(String id) {
        for (UpdateSite s : sites) {
            if (s.getId().equals(id)) {
                return s;
            }
        }
        return null;
    }