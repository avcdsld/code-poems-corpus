def foreachBatch(self, func):
        """
        Sets the output of the streaming query to be processed using the provided
        function. This is supported only the in the micro-batch execution modes (that is, when the
        trigger is not continuous). In every micro-batch, the provided function will be called in
        every micro-batch with (i) the output rows as a DataFrame and (ii) the batch identifier.
        The batchId can be used deduplicate and transactionally write the output
        (that is, the provided Dataset) to external systems. The output DataFrame is guaranteed
        to exactly same for the same batchId (assuming all operations are deterministic in the
        query).

        .. note:: Evolving.

        >>> def func(batch_df, batch_id):
        ...     batch_df.collect()
        ...
        >>> writer = sdf.writeStream.foreach(func)
        """

        from pyspark.java_gateway import ensure_callback_server_started
        gw = self._spark._sc._gateway
        java_import(gw.jvm, "org.apache.spark.sql.execution.streaming.sources.*")

        wrapped_func = ForeachBatchFunction(self._spark, func)
        gw.jvm.PythonForeachBatchHelper.callForeachBatch(self._jwrite, wrapped_func)
        ensure_callback_server_started(gw)
        return self