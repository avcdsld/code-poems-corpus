function where(collection, properties, first) {
    return (first && isEmpty(properties))
      ? undefined
      : (first ? find : filter)(collection, properties);
  }