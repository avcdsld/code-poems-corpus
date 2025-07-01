public static void setPropsInYamlFile(final String path, final File flowFile, final Props prop) {
    final DumperOptions options = new DumperOptions();
    options.setDefaultFlowStyle(FlowStyle.BLOCK);
    final NodeBean nodeBean = FlowLoaderUtils.setPropsInNodeBean(path, flowFile, prop);
    try (final BufferedWriter writer = Files
        .newBufferedWriter(flowFile.toPath(), StandardCharsets.UTF_8)) {
      new Yaml(options).dump(nodeBean, writer);
    } catch (final IOException e) {
      throw new ProjectManagerException(
          "Failed to set properties in flow file " + flowFile.getName());
    }
  }