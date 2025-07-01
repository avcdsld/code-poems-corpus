@WithBridgeMethods(value=Jenkins.class,castRequired=true)
    @Override public @Nonnull ItemGroup getParent() {
        if (parent == null) {
            throw new IllegalStateException("no parent set on " + getClass().getName() + "[" + name + "]");
        }
        return parent;
    }