def _split_generators(self, dl_manager):
    """Return the test split of Cifar10.

    Args:
      dl_manager: download manager object.

    Returns:
      test split.
    """
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={'data_dir': os.path.join(path, _DIRNAME)})
    ]