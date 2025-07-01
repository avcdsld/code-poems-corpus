public void normalize() {
        for (T key : keySet()) {
            setCount(key, getCount(key) / totalCount.get());
        }

        rebuildTotals();
    }