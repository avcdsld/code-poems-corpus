@Override
    @Deprecated
    public boolean add(T t) {
        try {
            return addSync(t);
        } finally {
            if(extensions!=null) {
                fireOnChangeListeners();
            }
        }
    }