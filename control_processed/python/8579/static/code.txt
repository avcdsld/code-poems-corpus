def completed_prefetch(self, blocking_wait=False, max_yield=999):
        """Similar to completed but only returns once the object is local.

        Assumes obj_id only is one id."""

        for worker, obj_id in self.completed(blocking_wait=blocking_wait):
            plasma_id = ray.pyarrow.plasma.ObjectID(obj_id.binary())
            (ray.worker.global_worker.raylet_client.fetch_or_reconstruct(
                [obj_id], True))
            self._fetching.append((worker, obj_id))

        remaining = []
        num_yielded = 0
        for worker, obj_id in self._fetching:
            plasma_id = ray.pyarrow.plasma.ObjectID(obj_id.binary())
            if (num_yielded < max_yield
                    and ray.worker.global_worker.plasma_client.contains(
                        plasma_id)):
                yield (worker, obj_id)
                num_yielded += 1
            else:
                remaining.append((worker, obj_id))
        self._fetching = remaining