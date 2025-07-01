public void expandParamPanelNode(String panelName) {
        DefaultMutableTreeNode node = getTreeNodeFromPanelName(panelName);
        if (node != null) {
            getTreeParam().expandPath(new TreePath(node.getPath()));
        }
    }