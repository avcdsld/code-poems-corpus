def delete_document(
        self,
        name,
        current_document=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a document.

        Example:
            >>> from google.cloud import firestore_v1beta1
            >>>
            >>> client = firestore_v1beta1.FirestoreClient()
            >>>
            >>> name = client.any_path_path('[PROJECT]', '[DATABASE]', '[DOCUMENT]', '[ANY_PATH]')
            >>>
            >>> client.delete_document(name)

        Args:
            name (str): The resource name of the Document to delete. In the format:
                ``projects/{project_id}/databases/{database_id}/documents/{document_path}``.
            current_document (Union[dict, ~google.cloud.firestore_v1beta1.types.Precondition]): An optional precondition on the document.
                The request will fail if this is set and not met by the target document.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.firestore_v1beta1.types.Precondition`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_document" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_document"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_document,
                default_retry=self._method_configs["DeleteDocument"].retry,
                default_timeout=self._method_configs["DeleteDocument"].timeout,
                client_info=self._client_info,
            )

        request = firestore_pb2.DeleteDocumentRequest(
            name=name, current_document=current_document
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_document"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )