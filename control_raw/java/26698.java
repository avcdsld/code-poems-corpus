public String buildPagingQuery(int inPageIndex) {
        this.setPageIndex(inPageIndex);
        String pageFilter = "\npage:\n" + "   size: " + pageSize + "\n" + "   start: " + pageIndex;
        this.setPagingQuery(this.getBasicQuery() + pageFilter);
        return this.getPagingQuery();
    }