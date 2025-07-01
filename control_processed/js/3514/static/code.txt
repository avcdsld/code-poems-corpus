function extractDomain (url) {
  // Find and remove protocol (e.g., http, ftp, etc.) to get domain.
  var domain = url.indexOf('://') > -1 ? url.split('/')[2] : url.split('/')[0];

  // Find and remove port number.
  return domain.substring(0, domain.indexOf(':'));
}