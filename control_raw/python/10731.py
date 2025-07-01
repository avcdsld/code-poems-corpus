def run_pipeline(self, pipeline, start_date, end_date):
        """
        Compute a pipeline.

        Parameters
        ----------
        pipeline : zipline.pipeline.Pipeline
            The pipeline to run.
        start_date : pd.Timestamp
            Start date of the computed matrix.
        end_date : pd.Timestamp
            End date of the computed matrix.

        Returns
        -------
        result : pd.DataFrame
            A frame of computed results.

            The ``result`` columns correspond to the entries of
            `pipeline.columns`, which should be a dictionary mapping strings to
            instances of :class:`zipline.pipeline.term.Term`.

            For each date between ``start_date`` and ``end_date``, ``result``
            will contain a row for each asset that passed `pipeline.screen`.
            A screen of ``None`` indicates that a row should be returned for
            each asset that existed each day.

        See Also
        --------
        :meth:`zipline.pipeline.engine.PipelineEngine.run_pipeline`
        :meth:`zipline.pipeline.engine.PipelineEngine.run_chunked_pipeline`
        """
        # See notes at the top of this module for a description of the
        # algorithm implemented here.
        if end_date < start_date:
            raise ValueError(
                "start_date must be before or equal to end_date \n"
                "start_date=%s, end_date=%s" % (start_date, end_date)

            )

        domain = self.resolve_domain(pipeline)

        graph = pipeline.to_execution_plan(
            domain, self._root_mask_term, start_date, end_date,
        )
        extra_rows = graph.extra_rows[self._root_mask_term]
        root_mask = self._compute_root_mask(
            domain, start_date, end_date, extra_rows,
        )
        dates, assets, root_mask_values = explode(root_mask)

        initial_workspace = self._populate_initial_workspace(
            {
                self._root_mask_term: root_mask_values,
                self._root_mask_dates_term: as_column(dates.values)
            },
            self._root_mask_term,
            graph,
            dates,
            assets,
        )

        results = self.compute_chunk(graph, dates, assets, initial_workspace)

        return self._to_narrow(
            graph.outputs,
            results,
            results.pop(graph.screen_name),
            dates[extra_rows:],
            assets,
        )