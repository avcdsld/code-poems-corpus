@RequirePOST
    public HttpResponse doSiteConfigure(@QueryParameter String site) throws IOException {
        Jenkins hudson = Jenkins.getInstance();
        hudson.checkPermission(CONFIGURE_UPDATECENTER);
        UpdateCenter uc = hudson.getUpdateCenter();
        PersistedList<UpdateSite> sites = uc.getSites();
        for (UpdateSite s : sites) {
            if (s.getId().equals(UpdateCenter.ID_DEFAULT))
                sites.remove(s);
        }
        sites.add(new UpdateSite(UpdateCenter.ID_DEFAULT, site));

        return new HttpRedirect("advanced");
    }