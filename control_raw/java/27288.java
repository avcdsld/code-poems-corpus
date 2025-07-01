private void processParentPage(PageWrapper parentPage, PageModificationContext context) {
        if (context.getDeletedPageKey() != null) {
            // We have a deleted page. Remove its pointer from the parent.
            parentPage.getPage().update(Collections.singletonList(PageEntry.noValue(context.getDeletedPageKey())));
            parentPage.markNeedsFirstKeyUpdate();
        } else {
            // Update parent page's child pointers for modified pages.
            val toUpdate = context.getUpdatedPagePointers().stream()
                                  .map(pp -> new PageEntry(pp.getKey(), serializePointer(pp)))
                                  .collect(Collectors.toList());
            parentPage.getPage().update(toUpdate);
        }
    }