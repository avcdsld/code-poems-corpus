public static <T> Iterator<T> readOnly(final Iterator<T> itr) {
        return new Iterator<T>() {
            public boolean hasNext() {
                return itr.hasNext();
            }

            public T next() {
                return itr.next();
            }

            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }