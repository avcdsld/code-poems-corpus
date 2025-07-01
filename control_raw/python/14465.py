def _to_dataframe_bqstorage(self, bqstorage_client, dtypes, progress_bar=None):
        """Use (faster, but billable) BQ Storage API to construct DataFrame."""
        if bigquery_storage_v1beta1 is None:
            raise ValueError(_NO_BQSTORAGE_ERROR)

        if "$" in self._table.table_id:
            raise ValueError(
                "Reading from a specific partition is not currently supported."
            )
        if "@" in self._table.table_id:
            raise ValueError(
                "Reading from a specific snapshot is not currently supported."
            )

        read_options = bigquery_storage_v1beta1.types.TableReadOptions()
        if self._selected_fields is not None:
            for field in self._selected_fields:
                read_options.selected_fields.append(field.name)

        session = bqstorage_client.create_read_session(
            self._table.to_bqstorage(),
            "projects/{}".format(self._project),
            read_options=read_options,
        )

        # We need to parse the schema manually so that we can rearrange the
        # columns.
        schema = json.loads(session.avro_schema.schema)
        columns = [field["name"] for field in schema["fields"]]

        # Avoid reading rows from an empty table. pandas.concat will fail on an
        # empty list.
        if not session.streams:
            return pandas.DataFrame(columns=columns)

        # Use _to_dataframe_finished to notify worker threads when to quit.
        # See: https://stackoverflow.com/a/29237343/101923
        self._to_dataframe_finished = False

        # Create a queue to track progress updates across threads.
        worker_queue = _NoopProgressBarQueue()
        progress_queue = None
        progress_thread = None
        if progress_bar is not None:
            worker_queue = queue.Queue()
            progress_queue = queue.Queue()
            progress_thread = threading.Thread(
                target=self._process_worker_updates, args=(worker_queue, progress_queue)
            )
            progress_thread.start()

        def get_frames(pool):
            frames = []

            # Manually submit jobs and wait for download to complete rather
            # than using pool.map because pool.map continues running in the
            # background even if there is an exception on the main thread.
            # See: https://github.com/googleapis/google-cloud-python/pull/7698
            not_done = [
                pool.submit(
                    self._to_dataframe_bqstorage_stream,
                    bqstorage_client,
                    dtypes,
                    columns,
                    session,
                    stream,
                    worker_queue,
                )
                for stream in session.streams
            ]

            while not_done:
                done, not_done = concurrent.futures.wait(
                    not_done, timeout=_PROGRESS_INTERVAL
                )
                frames.extend([future.result() for future in done])

                # The progress bar needs to update on the main thread to avoid
                # contention over stdout / stderr.
                self._process_progress_updates(progress_queue, progress_bar)

            return frames

        with concurrent.futures.ThreadPoolExecutor() as pool:
            try:
                frames = get_frames(pool)
            finally:
                # No need for a lock because reading/replacing a variable is
                # defined to be an atomic operation in the Python language
                # definition (enforced by the global interpreter lock).
                self._to_dataframe_finished = True

                # Shutdown all background threads, now that they should know to
                # exit early.
                pool.shutdown(wait=True)
                if progress_thread is not None:
                    progress_thread.join()

        # Update the progress bar one last time to close it.
        self._process_progress_updates(progress_queue, progress_bar)
        return pandas.concat(frames)