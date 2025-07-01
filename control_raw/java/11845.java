@SuppressWarnings({"ConstantConditions","deprecation"})
    @SuppressFBWarnings("RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE")
    public boolean removeActions(@Nonnull Class<? extends Action> clazz) {
        if (clazz == null) {
            throw new IllegalArgumentException("Action type must be non-null");
        }
        // CopyOnWriteArrayList does not support Iterator.remove, so need to do it this way:
        List<Action> old = new ArrayList<>();
        List<Action> current = getActions();
        for (Action a : current) {
            if (clazz.isInstance(a)) {
                old.add(a);
            }
        }
        return current.removeAll(old);
    }