def create_reference_image(
        self,
        parent,
        reference_image,
        reference_image_id,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates and returns a new ReferenceImage resource.

        The ``bounding_poly`` field is optional. If ``bounding_poly`` is not
        specified, the system will try to detect regions of interest in the
        image that are compatible with the product\_category on the parent
        product. If it is specified, detection is ALWAYS skipped. The system
        converts polygons into non-rotated rectangles.

        Note that the pipeline will resize the image if the image resolution is
        too large to process (above 50MP).

        Possible errors:

        -  Returns INVALID\_ARGUMENT if the image\_uri is missing or longer than
           4096 characters.
        -  Returns INVALID\_ARGUMENT if the product does not exist.
        -  Returns INVALID\_ARGUMENT if bounding\_poly is not provided, and
           nothing compatible with the parent product's product\_category is
           detected.
        -  Returns INVALID\_ARGUMENT if bounding\_poly contains more than 10
           polygons.

        Example:
            >>> from google.cloud import vision_v1p3beta1
            >>>
            >>> client = vision_v1p3beta1.ProductSearchClient()
            >>>
            >>> parent = client.product_path('[PROJECT]', '[LOCATION]', '[PRODUCT]')
            >>>
            >>> # TODO: Initialize `reference_image`:
            >>> reference_image = {}
            >>>
            >>> # TODO: Initialize `reference_image_id`:
            >>> reference_image_id = ''
            >>>
            >>> response = client.create_reference_image(parent, reference_image, reference_image_id)

        Args:
            parent (str): Resource name of the product in which to create the reference image.

                Format is ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``.
            reference_image (Union[dict, ~google.cloud.vision_v1p3beta1.types.ReferenceImage]): The reference image to create.
                If an image ID is specified, it is ignored.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.vision_v1p3beta1.types.ReferenceImage`
            reference_image_id (str): A user-supplied resource id for the ReferenceImage to be added. If set,
                the server will attempt to use this value as the resource id. If it is
                already in use, an error is returned with code ALREADY\_EXISTS. Must be
                at most 128 characters long. It cannot contain the character ``/``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.vision_v1p3beta1.types.ReferenceImage` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_reference_image" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_reference_image"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_reference_image,
                default_retry=self._method_configs["CreateReferenceImage"].retry,
                default_timeout=self._method_configs["CreateReferenceImage"].timeout,
                client_info=self._client_info,
            )

        request = product_search_service_pb2.CreateReferenceImageRequest(
            parent=parent,
            reference_image=reference_image,
            reference_image_id=reference_image_id,
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

        return self._inner_api_calls["create_reference_image"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )