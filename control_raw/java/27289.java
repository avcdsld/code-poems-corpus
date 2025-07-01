private CompletableFuture<PageWrapper> locatePage(ByteArraySegment key, PageCollection pageCollection, TimeoutTimer timer) {
        // Verify the sought key has the expected length.
        Preconditions.checkArgument(key.getLength() == this.leafPageConfig.getKeyLength(), "Invalid key length.");

        // Sanity check that our pageCollection has a somewhat correct view of the data index state. It is OK for it to
        // think the index length is less than what it actually is (since a concurrent update may have increased it), but
        // it is not a good sign if it thinks it's longer than the actual length.
        Preconditions.checkArgument(pageCollection.getIndexLength() <= this.state.get().length, "Unexpected PageCollection.IndexLength.");

        if (this.state.get().rootPageOffset == PagePointer.NO_OFFSET && pageCollection.getCount() == 0) {
            // No data. Return an empty (leaf) page, which will serve as the root for now.
            return CompletableFuture.completedFuture(pageCollection.insert(PageWrapper.wrapNew(createEmptyLeafPage(), null, null)));
        }

        // Locate the page by searching on the Key (within the page).
        return locatePage(page -> getPagePointer(key, page), page -> !page.isIndexPage(), pageCollection, timer);
    }