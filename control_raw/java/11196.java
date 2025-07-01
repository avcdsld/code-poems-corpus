@SuppressWarnings({"unchecked"})
    public static <U,T extends U> Iterator<T> subType(Iterator<U> itr, final Class<T> type) {
        return (Iterator)new FilterIterator<U>(itr) {
            protected boolean filter(U u) {
                return type.isInstance(u);
            }
        };
    }