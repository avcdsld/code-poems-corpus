def analyze_sentiment(
        self,
        document,
        encoding_type=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Analyzes the sentiment of the provided text.

        Example:
            >>> from google.cloud import language_v1
            >>>
            >>> client = language_v1.LanguageServiceClient()
            >>>
            >>> # TODO: Initialize `document`:
            >>> document = {}
            >>>
            >>> response = client.analyze_sentiment(document)

        Args:
            document (Union[dict, ~google.cloud.language_v1.types.Document]): Input document.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.language_v1.types.Document`
            encoding_type (~google.cloud.language_v1.types.EncodingType): The encoding type used by the API to calculate sentence offsets.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.language_v1.types.AnalyzeSentimentResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "analyze_sentiment" not in self._inner_api_calls:
            self._inner_api_calls[
                "analyze_sentiment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.analyze_sentiment,
                default_retry=self._method_configs["AnalyzeSentiment"].retry,
                default_timeout=self._method_configs["AnalyzeSentiment"].timeout,
                client_info=self._client_info,
            )

        request = language_service_pb2.AnalyzeSentimentRequest(
            document=document, encoding_type=encoding_type
        )
        return self._inner_api_calls["analyze_sentiment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )