protected OrderByElement cloneOrderByElement(OrderByElement orig, String alias) {
        return cloneOrderByElement(orig, new Column(alias));
    }