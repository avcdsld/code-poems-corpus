public static ImageInfo of(ImageId imageId, ImageConfiguration configuration) {
    return newBuilder(imageId, configuration).build();
  }