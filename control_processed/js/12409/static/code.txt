function getMetaData (type, imageId) {
  // Invoke each provider in priority order until one returns something
  for (let i = 0; i < providers.length; i++) {
    const result = providers[i].provider(type, imageId);

    if (result !== undefined) {
      return result;
    }
  }
}