public static <T extends MessageLite> Metadata.BinaryMarshaller<T> metadataMarshaller(
      T defaultInstance) {
    return new MetadataMarshaller<>(defaultInstance);
  }