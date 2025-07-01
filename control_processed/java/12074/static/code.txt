private int at(long t) {
        SortedMap<Long, int[]> head = data.subMap(t,Long.MAX_VALUE);
        if (head.isEmpty()) return 0;
        return data.get(head.firstKey())[0];
    }