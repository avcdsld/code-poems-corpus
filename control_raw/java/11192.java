public static List<Integer> sequence(final int start, int end, final int step) {

        final int size = (end-start)/step;
        if(size<0)  throw new IllegalArgumentException("List size is negative");

        return new AbstractList<Integer>() {
            public Integer get(int index) {
                if(index<0 || index>=size)
                    throw new IndexOutOfBoundsException();
                return start+index*step;
            }

            public int size() {
                return size;
            }
        };
    }