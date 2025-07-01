public ApiListingBuilder availableTags(Set<Tag> availableTags) {
    this.tagLookup.putAll(nullToEmptySet(availableTags).stream().collect(toMap(Tag::getName, identity())));
    return this;
  }