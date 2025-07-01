public void connect(List<Tree> children) {
        this.children = children;
        for (Tree t : children)
            t.setParent(this);
    }