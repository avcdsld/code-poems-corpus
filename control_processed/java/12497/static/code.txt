@Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
        for (Class<?> t = type.getRawType(); (t != Object.class) && (t.getSuperclass() != null); t = t.getSuperclass()) {
            for (Method m : t.getDeclaredMethods()) {
                if (m.isAnnotationPresent(PostConstruct.class)) {
                    m.setAccessible(true);
                    TypeAdapter<T> delegate = gson.getDelegateAdapter(this, type);
                    return new PostConstructAdapter<T>(delegate, m);
                }
            }
        }
        return null;
    }