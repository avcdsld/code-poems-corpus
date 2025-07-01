synchronized void collectPages(Collection<Long> offsets, Collection<PageWrapper> target) {
        offsets.forEach(offset -> {
            PageWrapper p = this.pageByOffset.getOrDefault(offset, null);
            if (p != null) {
                target.add(p);
            }
        });
    }