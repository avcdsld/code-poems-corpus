TreeMap<Integer,BuildReference<R>> all() {
        if (!fullyLoaded) {
            synchronized (this) {
                if (!fullyLoaded) {
                    Index copy = copy();
                    for (Integer number : numberOnDisk) {
                        if (!copy.byNumber.containsKey(number))
                            load(number, copy);
                    }
                    index = copy;
                    fullyLoaded = true;
                }
            }
        }
        return index.byNumber;
    }