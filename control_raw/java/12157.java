public synchronized int findNumber(@Nonnull String id) {
        Integer number = idToNumber.get(id);
        return number != null ? number : 0;
    }