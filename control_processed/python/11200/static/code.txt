def _generate_examples(self, dat_path, cat_path, info_path):
    """Generate examples for the Smallnorb dataset.

    Args:
      dat_path: Path to dat file of the chunk.
      cat_path: Path to cat file of the chunk.
      info_path: Path to info file of the chunk.

    Yields:
      Dictionaries with images and the different labels.
    """
    dat_arr, cat_arr, info_arr = _load_chunk(dat_path, cat_path, info_path)

    for image, category, info_vec in moves.zip(dat_arr, cat_arr, info_arr):
      yield {
          "image": image[0],
          "image2": image[1],
          "label_category": category,
          "instance": info_vec[0],
          "label_elevation": info_vec[1],
          "label_azimuth": info_vec[2],
          "label_lighting": info_vec[3],
      }