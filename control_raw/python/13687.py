def block_widths(self):
        """Gets the widths of the blocks.

        Note: This works with the property structure `_widths_cache` to avoid
            having to recompute these values each time they are needed.
        """
        if self._widths_cache is None:
            try:
                # The first column will have the correct lengths. We have an
                # invariant that requires that all blocks be the same width in a
                # column of blocks.
                self._widths_cache = np.array(
                    ray.get([obj.width().oid for obj in self._partitions_cache[0]])
                    if len(self._partitions_cache) > 0
                    else []
                )
            except RayTaskError as e:
                handle_ray_task_error(e)
        return self._widths_cache