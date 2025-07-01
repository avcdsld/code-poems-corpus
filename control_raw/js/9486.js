function(providers, method_definition) {
  if (!Array.isArray(providers)) {
    return null;
  }
  var interceptors = [];
  for (var i = 0; i < providers.length; i++) {
    var provider = providers[i];
    var interceptor = provider(method_definition);
    if (interceptor) {
      interceptors.push(interceptor);
    }
  }
  return interceptors;
}