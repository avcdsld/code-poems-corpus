def partition_expiration(self):
        """Union[int, None]: Expiration time in milliseconds for a partition.

        If :attr:`partition_expiration` is set and :attr:`type_` is
        not set, :attr:`type_` will default to
        :attr:`~google.cloud.bigquery.table.TimePartitioningType.DAY`.
        """
        warnings.warn(
            "This method will be deprecated in future versions. Please use "
            "Table.time_partitioning.expiration_ms instead.",
            PendingDeprecationWarning,
            stacklevel=2,
        )
        if self.time_partitioning is not None:
            return self.time_partitioning.expiration_ms