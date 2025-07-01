def create_transfer_config(
        self,
        parent,
        transfer_config,
        authorization_code=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new data transfer configuration.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `transfer_config`:
            >>> transfer_config = {}
            >>>
            >>> response = client.create_transfer_config(parent, transfer_config)

        Args:
            parent (str): The BigQuery project id where the transfer configuration should be
                created. Must be in the format
                /projects/{project\_id}/locations/{location\_id} If specified location
                and location of the destination bigquery dataset do not match - the
                request will fail.
            transfer_config (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.TransferConfig]): Data transfer configuration to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig`
            authorization_code (str): Optional OAuth2 authorization code to use with this transfer
                configuration. This is required if new credentials are needed, as
                indicated by ``CheckValidCreds``. In order to obtain
                authorization\_code, please make a request to
                https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?client\_id=&scope=<data\_source\_scopes>&redirect\_uri=<redirect\_uri>

                -  client\_id should be OAuth client\_id of BigQuery DTS API for the
                   given data source returned by ListDataSources method.
                -  data\_source\_scopes are the scopes returned by ListDataSources
                   method.
                -  redirect\_uri is an optional parameter. If not specified, then
                   authorization code is posted to the opener of authorization flow
                   window. Otherwise it will be sent to the redirect uri. A special
                   value of urn:ietf:wg:oauth:2.0:oob means that authorization code
                   should be returned in the title bar of the browser, with the page
                   text prompting the user to copy the code and paste it in the
                   application.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_transfer_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_transfer_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_transfer_config,
                default_retry=self._method_configs["CreateTransferConfig"].retry,
                default_timeout=self._method_configs["CreateTransferConfig"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.CreateTransferConfigRequest(
            parent=parent,
            transfer_config=transfer_config,
            authorization_code=authorization_code,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_transfer_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )