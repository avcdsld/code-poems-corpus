def preprocess_example(self, example, mode, hparams):
    """Runtime preprocessing, e.g., resize example["frame"]."""
    if getattr(hparams, "preprocess_resize_frames", None) is not None:
      example["frame"] = tf.image.resize_images(
          example["frame"], hparams.preprocess_resize_frames,
          tf.image.ResizeMethod.BILINEAR)
    return example