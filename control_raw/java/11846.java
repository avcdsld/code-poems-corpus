@SuppressWarnings({"ConstantConditions", "deprecation"})
    @SuppressFBWarnings("RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE")
    public boolean replaceActions(@Nonnull Class<? extends Action> clazz, @Nonnull Action a) {
        if (clazz == null) {
            throw new IllegalArgumentException("Action type must be non-null");
        }
        if (a == null) {
            throw new IllegalArgumentException("Action must be non-null");
        }
        // CopyOnWriteArrayList does not support Iterator.remove, so need to do it this way:
        List<Action> old = new ArrayList<>();
        List<Action> current = getActions();
        boolean found = false;
        for (Action a1 : current) {
            if (!found) {
                if (a.equals(a1)) {
                    found = true;
                } else if (clazz.isInstance(a1)) {
                    old.add(a1);
                }
            } else if (clazz.isInstance(a1) && !a.equals(a1)) {
                old.add(a1);
            }
        }
        current.removeAll(old);
        if (!found) {
            addAction(a);
        }
        return !(old.isEmpty() && found);
    }