private void processModifiedPage(PageModificationContext context) {
        PageWrapper page = context.getPageWrapper();
        boolean emptyPage = page.getPage().getCount() == 0;
        ByteArraySegment pageKey = page.getPageKey();
        if (emptyPage && page.getParent() != null) {
            // This page is empty. Remove it from the PageCollection (so we don't write it back to our data source)
            // and remember its Page Key so we can delete its pointer from its parent page.
            context.getPageCollection().remove(page);
            context.setDeletedPageKey(pageKey);
        } else {
            // This page needs to be kept around.
            if (emptyPage && page.getPage().getConfig().isIndexPage()) {
                // We have an empty Index Root Page. We must convert this to a Leaf Page before moving on.
                page.setPage(createEmptyLeafPage());
            }

            // Assign a new offset to the page and record its new Page Pointer.
            context.pageCollection.complete(page);
            page.setMinOffset(calculateMinOffset(page));
            context.updatePagePointer(new PagePointer(pageKey, page.getOffset(), page.getPage().getLength(), page.getMinOffset()));
        }
    }