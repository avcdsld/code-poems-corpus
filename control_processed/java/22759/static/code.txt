public List<String> getVariables() {
    return this.templateChunks.stream()
        .filter(templateChunk -> Expression.class.isAssignableFrom(templateChunk.getClass()))
        .map(templateChunk -> ((Expression) templateChunk).getName())
        .filter(Objects::nonNull)
        .collect(Collectors.toList());
  }