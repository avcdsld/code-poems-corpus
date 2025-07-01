def getStorageLevel(self):
        """
        Get the RDD's current storage level.

        >>> rdd1 = sc.parallelize([1,2])
        >>> rdd1.getStorageLevel()
        StorageLevel(False, False, False, False, 1)
        >>> print(rdd1.getStorageLevel())
        Serialized 1x Replicated
        """
        java_storage_level = self._jrdd.getStorageLevel()
        storage_level = StorageLevel(java_storage_level.useDisk(),
                                     java_storage_level.useMemory(),
                                     java_storage_level.useOffHeap(),
                                     java_storage_level.deserialized(),
                                     java_storage_level.replication())
        return storage_level