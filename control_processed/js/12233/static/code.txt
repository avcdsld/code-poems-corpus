function _createSync(siteId) {
  const ttxSettings = config.getConfig('ttxSettings');
  const syncUrl = (ttxSettings && ttxSettings.syncUrl) || SYNC_ENDPOINT;

  return {
    type: 'iframe',
    url: `${syncUrl}&id=${siteId}`
  }
}