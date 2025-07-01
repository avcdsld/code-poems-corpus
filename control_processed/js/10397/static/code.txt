function onActivate(event) {
  // Delete old caches to save space.
  const dropOldCaches = async () => {
    const cacheNames = await caches.keys();

    // Return true on all the caches we want to clean up.
    // Note that caches are shared across the origin, so only remove
    // caches we are sure we created.
    const cleanTheseUp = cacheNames.filter((cacheName) =>
        cacheName.startsWith(CACHE_NAME_PREFIX) && cacheName != CACHE_NAME);

    const cleanUpPromises =
        cleanTheseUp.map((cacheName) => caches.delete(cacheName));

    await Promise.all(cleanUpPromises);
  };

  event.waitUntil(dropOldCaches());
}