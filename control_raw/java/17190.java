public void incrementCount(F first, S second, double inc) {
        Counter<S> counter = maps.get(first);
        if (counter == null) {
            counter = new Counter<S>();
            maps.put(first, counter);
        }

        counter.incrementCount(second, inc);
    }