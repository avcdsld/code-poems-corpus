function getCachePathCandidates() {
  return [
    process.env.npm_config_FIS_binary_cache,
    process.env.npm_config_cache,
  ].filter(function(_) { return _; });
}