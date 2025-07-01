public synchronized static <T> T get(Object id)
    {
        SoftReference reference = pool.get(id);
        if (reference == null) return null;
        return (T) reference.get();
    }