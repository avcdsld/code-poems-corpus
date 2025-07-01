protected static SiteNode getSiteNode(HistoryReference historyReference) {
        SiteNode sn = historyReference.getSiteNode();
        if (sn == null) {
            sn = Model.getSingleton().getSession().getSiteTree().getSiteNode(historyReference.getHistoryId());
        }
        return sn;
    }