def list_traces(
        self,
        project_id=None,
        view=None,
        page_size=None,
        start_time=None,
        end_time=None,
        filter_=None,
        order_by=None,
        page_token=None,
    ):
        """
        Returns of a list of traces that match the filter conditions.

        Args:
            project_id (Optional[str]): ID of the Cloud project where the trace
                data is stored.

            view (Optional[~google.cloud.trace_v1.gapic.enums.
                ListTracesRequest.ViewType]): Type of data returned for traces
                in the list. Default is ``MINIMAL``.

            page_size (Optional[int]): Maximum number of traces to return. If
                not specified or <= 0, the implementation selects a reasonable
                value. The implementation may return fewer traces than the
                requested page size.

            start_time (Optional[~datetime.datetime]): Start of the time
                interval (inclusive) during which the trace data was collected
                from the application.

            end_time (Optional[~datetime.datetime]): End of the time interval
                (inclusive) during which the trace data was collected from the
                application.

            filter_ (Optional[str]): An optional filter for the request.

            order_by (Optional[str]): Field used to sort the returned traces.

            page_token (Optional[str]): opaque marker for the next "page" of
                entries. If not passed, the API will return the first page of
                entries.

        Returns:
            A  :class:`~google.api_core.page_iterator.Iterator` of traces that
            match the specified filter conditions.
        """
        if project_id is None:
            project_id = self.project

        if start_time is not None:
            start_time = _datetime_to_pb_timestamp(start_time)

        if end_time is not None:
            end_time = _datetime_to_pb_timestamp(end_time)

        return self.trace_api.list_traces(
            project_id=project_id,
            view=view,
            page_size=page_size,
            start_time=start_time,
            end_time=end_time,
            filter_=filter_,
            order_by=order_by,
            page_token=page_token,
        )