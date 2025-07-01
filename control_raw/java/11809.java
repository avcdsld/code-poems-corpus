@RequirePOST
    public void doUpgrade(StaplerResponse rsp) throws IOException, ServletException {
        HudsonUpgradeJob job = new HudsonUpgradeJob(getCoreSource(), Jenkins.getAuthentication());
        if(!Lifecycle.get().canRewriteHudsonWar()) {
            sendError("Jenkins upgrade not supported in this running mode");
            return;
        }

        LOGGER.info("Scheduling the core upgrade");
        addJob(job);
        rsp.sendRedirect2(".");
    }