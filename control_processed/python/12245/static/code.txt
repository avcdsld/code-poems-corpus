def get_target_delegate(
        self, target: Any, request: httputil.HTTPServerRequest, **target_params: Any
    ) -> Optional[httputil.HTTPMessageDelegate]:
        """Returns an instance of `~.httputil.HTTPMessageDelegate` for a
        Rule's target. This method is called by `~.find_handler` and can be
        extended to provide additional target types.

        :arg target: a Rule's target.
        :arg httputil.HTTPServerRequest request: current request.
        :arg target_params: additional parameters that can be useful
            for `~.httputil.HTTPMessageDelegate` creation.
        """
        if isinstance(target, Router):
            return target.find_handler(request, **target_params)

        elif isinstance(target, httputil.HTTPServerConnectionDelegate):
            assert request.connection is not None
            return target.start_request(request.server_connection, request.connection)

        elif callable(target):
            assert request.connection is not None
            return _CallableAdapter(
                partial(target, **target_params), request.connection
            )

        return None