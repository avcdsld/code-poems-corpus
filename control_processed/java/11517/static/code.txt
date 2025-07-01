public void addNode(final @Nonnull Node node) throws IOException {
        Node oldNode = nodes.get(node.getNodeName());
        if (node != oldNode) {
            // TODO we should not need to lock the queue for adding nodes but until we have a way to update the
            // computer list for just the new node
            Queue.withLock(new Runnable() {
                @Override
                public void run() {
                    nodes.put(node.getNodeName(), node);
                    jenkins.updateComputerList();
                    jenkins.trimLabels();
                }
            });
            // TODO there is a theoretical race whereby the node instance is updated/removed after lock release
            try {
                persistNode(node);
            } catch (IOException | RuntimeException e) {
                // JENKINS-50599: If persisting the node throws an exception, we need to remove the node from
                // memory before propagating the exception.
                Queue.withLock(new Runnable() {
                    @Override
                    public void run() {
                        nodes.compute(node.getNodeName(), (ignoredNodeName, ignoredNode) -> oldNode);
                        jenkins.updateComputerList();
                        jenkins.trimLabels();
                    }
                });
                throw e;
            }
            NodeListener.fireOnCreated(node);
        }
    }