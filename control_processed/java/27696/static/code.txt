synchronized List<PageWrapper> getPagesSortedByOffset() {
        return this.pageByOffset
                .values().stream()
                .sorted(Comparator.comparingLong(PageWrapper::getOffset))
                .collect(Collectors.toList());
    }