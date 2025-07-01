def load(path, size=None):
        """
        Args:
            size (int): total number of records. If not provided, the returned dataflow will have no `__len__()`.
                It's needed because this metadata is not stored in the TFRecord file.
        """
        gen = tf.python_io.tf_record_iterator(path)
        ds = DataFromGenerator(gen)
        ds = MapData(ds, loads)
        if size is not None:
            ds = FixedSizeData(ds, size)
        return ds