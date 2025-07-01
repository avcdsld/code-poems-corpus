function getBuildOptionsFromConfig(ctx) {
  var chcpBuildOptionsFilePath = path.join(ctx.opts.projectRoot, OPTIONS_FILE_NAME);

  return readObjectFromFile(chcpBuildOptionsFilePath);
}