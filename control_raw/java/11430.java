@Restricted(DoNotUse.class)
    @Exported
    public @Nonnull String getDescription() {
        Node node = getNode();
        return (node != null) ? node.getNodeDescription() : null;
    }