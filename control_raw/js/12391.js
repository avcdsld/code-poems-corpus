function purgeCacheIfNecessary () {
  // If max cache size has not been exceeded, do nothing
  if (cacheSizeInBytes <= maximumSizeInBytes) {
    return;
  }

  // Cache size has been exceeded, create list of images sorted by timeStamp
  // So we can purge the least recently used image
  function compare (a, b) {
    if (a.timeStamp > b.timeStamp) {
      return -1;
    }
    if (a.timeStamp < b.timeStamp) {
      return 1;
    }

    return 0;
  }
  cachedImages.sort(compare);

  // Remove images as necessary)
  while (cacheSizeInBytes > maximumSizeInBytes) {
    const lastCachedImage = cachedImages[cachedImages.length - 1];
    const imageId = lastCachedImage.imageId;

    removeImageLoadObject(imageId);

    triggerEvent(events, EVENTS.IMAGE_CACHE_PROMISE_REMOVED, { imageId });
  }

  const cacheInfo = getCacheInfo();

  triggerEvent(events, EVENTS.IMAGE_CACHE_FULL, cacheInfo);
}