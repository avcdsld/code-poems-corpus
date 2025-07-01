function extractOriginHeaders_(headers) {
    const result = {
      isSameOrigin: false,
    };
    for (const key in headers) {
      if (headers.hasOwnProperty(key)) {
        const normalizedKey = key.toLowerCase();
        // for same-origin requests where the Origin header is missing, AMP sets the amp-same-origin header
        if (normalizedKey === 'amp-same-origin') {
          result.isSameOrigin = true;
          return result;
        }
        // use the origin header otherwise
        if (normalizedKey === 'origin') {
          result.origin = headers[key];
          return result;
        }
      }
    }
    return null;
  }