def show_and_save_image(img, save_path):
  """Shows an image using matplotlib and saves it."""
  try:
    import matplotlib.pyplot as plt  # pylint: disable=g-import-not-at-top
  except ImportError as e:
    tf.logging.warning(
        "Showing and saving an image requires matplotlib to be "
        "installed: %s", e)
    raise NotImplementedError("Image display and save not implemented.")
  plt.imshow(img)
  with tf.gfile.Open(save_path, "wb") as sp:
    plt.savefig(sp)