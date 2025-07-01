def map_across_blocks(self, map_func):
        """Applies `map_func` to every partition.

        Args:
            map_func: The function to apply.

        Returns:
            A new BaseFrameManager object, the type of object that called this.
        """
        preprocessed_map_func = self.preprocess_func(map_func)
        new_partitions = np.array(
            [
                [part.apply(preprocessed_map_func) for part in row_of_parts]
                for row_of_parts in self.partitions
            ]
        )
        return self.__constructor__(new_partitions)