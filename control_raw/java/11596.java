public AnnotatedLargeText obtainLog() {
        WeakReference<AnnotatedLargeText> l = log;
        if(l==null) return null;
        return l.get();
    }