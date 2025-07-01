function getShareData(terria) {
  const initSources = terria.initSources.slice();

  addUserAddedCatalog(terria, initSources);
  addSharedMembers(terria, initSources);
  addViewSettings(terria, initSources);
  addFeaturePicking(terria, initSources);
  addLocationMarker(terria, initSources);

  return {
    version: "0.0.05",
    initSources: initSources
  };
}