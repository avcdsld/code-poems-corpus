function getHeaders(config) {
  const headers = { 'X-Presto-User': config.user };
  if (config.catalog) {
    headers['X-Presto-Catalog'] = config.catalog;
  }
  if (config.schema) {
    headers['X-Presto-Schema'] = config.schema;
  }
  return headers;
}