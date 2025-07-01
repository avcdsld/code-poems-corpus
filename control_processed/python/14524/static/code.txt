def copy_table(
        self,
        sources,
        destination,
        job_id=None,
        job_id_prefix=None,
        location=None,
        project=None,
        job_config=None,
        retry=DEFAULT_RETRY,
    ):
        """Copy one or more tables to another table.

        See
        https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#configuration.copy

        Arguments:
            sources (Union[ \
                :class:`~google.cloud.bigquery.table.Table`, \
                :class:`~google.cloud.bigquery.table.TableReference`, \
                str, \
                Sequence[ \
                    Union[ \
                        :class:`~google.cloud.bigquery.table.Table`, \
                        :class:`~google.cloud.bigquery.table.TableReference`, \
                        str, \
                    ] \
                ], \
            ]):
                Table or tables to be copied.
            destination (Union[
                :class:`~google.cloud.bigquery.table.Table`, \
                :class:`~google.cloud.bigquery.table.TableReference`, \
                str, \
            ]):
                Table into which data is to be copied.

        Keyword Arguments:
            job_id (str): (Optional) The ID of the job.
            job_id_prefix (str)
                (Optional) the user-provided prefix for a randomly generated
                job ID. This parameter will be ignored if a ``job_id`` is
                also given.
            location (str):
                Location where to run the job. Must match the location of any
                source table as well as the destination table.
            project (str):
                Project ID of the project of where to run the job. Defaults
                to the client's project.
            job_config (google.cloud.bigquery.job.CopyJobConfig):
                (Optional) Extra configuration options for the job.
            retry (google.api_core.retry.Retry):
                (Optional) How to retry the RPC.

        Returns:
            google.cloud.bigquery.job.CopyJob: A new copy job instance.
        """
        job_id = _make_job_id(job_id, job_id_prefix)

        if project is None:
            project = self.project

        if location is None:
            location = self.location

        job_ref = job._JobReference(job_id, project=project, location=location)

        # sources can be one of many different input types. (string, Table,
        # TableReference, or a sequence of any of those.) Convert them all to a
        # list of TableReferences.
        #
        # _table_arg_to_table_ref leaves lists unmodified.
        sources = _table_arg_to_table_ref(sources, default_project=self.project)

        if not isinstance(sources, collections_abc.Sequence):
            sources = [sources]

        sources = [
            _table_arg_to_table_ref(source, default_project=self.project)
            for source in sources
        ]

        destination = _table_arg_to_table_ref(destination, default_project=self.project)

        copy_job = job.CopyJob(
            job_ref, sources, destination, client=self, job_config=job_config
        )
        copy_job._begin(retry=retry)

        return copy_job