function getUrl(endpoint) {
    var useInternal = typeof options.useInternal === 'boolean' ?
      options.useInternal : false;

    return useInternal && endpoint.internalURL
      ? endpoint.internalURL
      : ((typeof options.useAdmin === 'boolean' && options.useAdmin && endpoint.adminURL) ?
        endpoint.adminURL : endpoint.publicURL);
  }