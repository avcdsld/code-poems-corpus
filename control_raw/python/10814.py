def from_file(cls, h5_file):
        """
        Construct from an h5py.File.

        Parameters
        ----------
        h5_file : h5py.File
            An HDF5 daily pricing file.
        """
        return cls({
            country: HDF5DailyBarReader.from_file(h5_file, country)
            for country in h5_file.keys()
        })