def _recursive_merged_items(self, index):
        """
        merge the partitioned items and return the as iterator

        If one partition can not be fit in memory, then them will be
        partitioned and merged recursively.
        """
        subdirs = [os.path.join(d, "parts", str(index)) for d in self.localdirs]
        m = ExternalMerger(self.agg, self.memory_limit, self.serializer, subdirs,
                           self.scale * self.partitions, self.partitions, self.batch)
        m.pdata = [{} for _ in range(self.partitions)]
        limit = self._next_limit()

        for j in range(self.spills):
            path = self._get_spill_dir(j)
            p = os.path.join(path, str(index))
            with open(p, 'rb') as f:
                m.mergeCombiners(self.serializer.load_stream(f), 0)

            if get_used_memory() > limit:
                m._spill()
                limit = self._next_limit()

        return m._external_items()