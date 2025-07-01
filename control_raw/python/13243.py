def put(self, rank, val):
        """
        Args:
            rank(int): rank of th element. All elements must have different ranks.
            val: an object
        """
        idx = bisect.bisect(self.ranks, rank)
        self.ranks.insert(idx, rank)
        self.data.insert(idx, val)