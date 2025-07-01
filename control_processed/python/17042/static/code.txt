def hash(self, seed=0):
        """
        Returns an SArray with a hash of each element. seed can be used
        to change the hash function to allow this method to be used for
        random number generation.

        Parameters
        ----------
        seed : int
            Defaults to 0. Can be changed to different values to get
            different hash results.

        Returns
        -------
        out : SArray
            An integer SArray with a hash value for each element. Identical
            elements are hashed to the same value
        """
        with cython_context():
            return SArray(_proxy=self.__proxy__.hash(seed))