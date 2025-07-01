function requestMetadata (context, router) {
  router = router || context.router;

  return [
    swaggerMetadata,
    swaggerApiMetadata,
    swaggerPathMetadata,
    swaggerOperationMetadata,
    swaggerParamsMetadata,
    swaggerSecurityMetadata
  ];

  /**
   * Sets `req.swagger.api`
   */
  function swaggerApiMetadata (req, res, next) {
    // Only set req.swagger.api if the request is under the API's basePath
    if (context.api) {
      let basePath = util.normalizePath(context.api.basePath, router);
      let reqPath = util.normalizePath(req.path, router);
      if (_.startsWith(reqPath, basePath)) {
        req.swagger.api = context.api;
      }
    }

    next();
  }

  /**
   * Sets `req.swagger.path`
   */
  function swaggerPathMetadata (req, res, next) {
    if (req.swagger.api) {
      let relPath = getRelativePath(req);
      let relPathNormalized = util.normalizePath(relPath, router);

      // Search for a matching path
      Object.keys(req.swagger.api.paths).some((swaggerPath) => {
        let swaggerPathNormalized = util.normalizePath(swaggerPath, router);

        if (swaggerPathNormalized === relPathNormalized) {
          // We found an exact match (i.e. a path with no parameters)
          req.swagger.path = req.swagger.api.paths[swaggerPath];
          req.swagger.pathName = swaggerPath;
          return true;
        }
        else if (req.swagger.path === null && pathMatches(relPathNormalized, swaggerPathNormalized)) {
          // We found a possible match, but keep searching in case we find an exact match
          req.swagger.path = req.swagger.api.paths[swaggerPath];
          req.swagger.pathName = swaggerPath;
        }
      });

      if (req.swagger.path) {
        util.debug("%s %s matches Swagger path %s", req.method, req.path, req.swagger.pathName);
      }
      else {
        util.warn('WARNING! Unable to find a Swagger path that matches "%s"', req.path);
      }
    }

    next();
  }
}