protected static boolean changed(Object oldObj, Object newObj) {
        return oldObj == null ?
            newObj != null :
            !oldObj.equals(newObj);
    }