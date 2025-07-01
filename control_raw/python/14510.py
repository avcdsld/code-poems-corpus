def list_models(
        self, dataset, max_results=None, page_token=None, retry=DEFAULT_RETRY
    ):
        """[Beta] List models in the dataset.

        See
        https://cloud.google.com/bigquery/docs/reference/rest/v2/models/list

        Args:
            dataset (Union[ \
                :class:`~google.cloud.bigquery.dataset.Dataset`, \
                :class:`~google.cloud.bigquery.dataset.DatasetReference`, \
                str, \
            ]):
                A reference to the dataset whose models to list from the
                BigQuery API. If a string is passed in, this method attempts
                to create a dataset reference from a string using
                :func:`google.cloud.bigquery.dataset.DatasetReference.from_string`.
            max_results (int):
                (Optional) Maximum number of models to return. If not passed,
                defaults to a value set by the API.
            page_token (str):
                (Optional) Token representing a cursor into the models. If
                not passed, the API will return the first page of models. The
                token marks the beginning of the iterator to be returned and
                the value of the ``page_token`` can be accessed at
                ``next_page_token`` of the
                :class:`~google.api_core.page_iterator.HTTPIterator`.
            retry (:class:`google.api_core.retry.Retry`):
                (Optional) How to retry the RPC.

         Returns:
            google.api_core.page_iterator.Iterator:
                Iterator of
                :class:`~google.cloud.bigquery.model.Model` contained
                within the requested dataset.
        """
        if isinstance(dataset, str):
            dataset = DatasetReference.from_string(
                dataset, default_project=self.project
            )

        if not isinstance(dataset, (Dataset, DatasetReference)):
            raise TypeError("dataset must be a Dataset, DatasetReference, or string")

        path = "%s/models" % dataset.path
        result = page_iterator.HTTPIterator(
            client=self,
            api_request=functools.partial(self._call_api, retry),
            path=path,
            item_to_value=_item_to_model,
            items_key="models",
            page_token=page_token,
            max_results=max_results,
        )
        result.dataset = dataset
        return result