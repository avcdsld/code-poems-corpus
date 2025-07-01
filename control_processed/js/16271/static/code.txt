function urlResolveFix (couchUrl, dbName) {
  if (/[^/]$/.test(couchUrl)) {
    couchUrl += '/'
  }
  return u.resolve(couchUrl, dbName)
}