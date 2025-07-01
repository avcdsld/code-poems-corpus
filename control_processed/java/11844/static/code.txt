@SuppressWarnings("deprecation")
    public boolean removeAction(@Nullable Action a) {
        if (a == null) {
            return false;
        }
        // CopyOnWriteArrayList does not support Iterator.remove, so need to do it this way:
        return getActions().removeAll(Collections.singleton(a));
    }