static Iterator<Page> lazySearch(final Wikipedia wikipedia, final String query) {
    final Response<Page> first = wikipedia.search(query);
    if (first.nextOffset == null) {
      return first.iterator();
    }
    return new Iterator<Page>() {
      Iterator<Page> current = first.iterator();
      Long nextOffset = first.nextOffset;

      @Override
      public boolean hasNext() {
        while (!current.hasNext() && nextOffset != null) {
          System.out.println("Wow.. even more results than " + nextOffset);
          Response<Page> nextPage = wikipedia.resumeSearch(query, nextOffset);
          current = nextPage.iterator();
          nextOffset = nextPage.nextOffset;
        }
        return current.hasNext();
      }

      @Override
      public Page next() {
        return current.next();
      }

      @Override
      public void remove() {
        throw new UnsupportedOperationException();
      }
    };
  }