function validateCubemapSrc (src, cb) {
  var aCubemap;
  var cubemapSrcRegex = '';
  var i;
  var urls;
  var validatedUrls = [];

  for (i = 0; i < 5; i++) {
    cubemapSrcRegex += '(url\\((?:[^\\)]+)\\),\\s*)';
  }
  cubemapSrcRegex += '(url\\((?:[^\\)]+)\\)\\s*)';
  urls = src.match(new RegExp(cubemapSrcRegex));

  // `src` is a comma-separated list of URLs.
  // In this case, re-use validateSrc for each side of the cube.
  function isImageCb (url) {
    validatedUrls.push(url);
    if (validatedUrls.length === 6) {
      cb(validatedUrls);
    }
  }
  if (urls) {
    for (i = 1; i < 7; i++) {
      validateSrc(parseUrl(urls[i]), isImageCb);
    }
    return;
  }

  // `src` is a query selector to <a-cubemap> containing six $([src])s.
  aCubemap = validateAndGetQuerySelector(src);
  if (!aCubemap) { return; }
  if (aCubemap.tagName === 'A-CUBEMAP' && aCubemap.srcs) {
    return cb(aCubemap.srcs);
  }
  // Else if aCubeMap is not a <a-cubemap>.
  warn('Selector "%s" does not point to <a-cubemap>', src);
}