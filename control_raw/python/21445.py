def mget(self, body, doc_type=None, index=None, params=None):
        """
        Get multiple documents based on an index, type (optional) and ids.
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-multi-get.html>`_

        :arg body: Document identifiers; can be either `docs` (containing full
            document information) or `ids` (when index and type is provided in
            the URL.
        :arg index: The name of the index
        :arg _source: True or false to return the _source field or not, or a
            list of fields to return
        :arg _source_exclude: A list of fields to exclude from the returned
            _source field
        :arg _source_include: A list of fields to extract and return from the
            _source field
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg realtime: Specify whether to perform the operation in realtime or
            search mode
        :arg refresh: Refresh the shard containing the document before
            performing the operation
        :arg routing: Specific routing value
        :arg stored_fields: A comma-separated list of stored fields to return in
            the response
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")
        return self.transport.perform_request(
            "GET", _make_path(index, doc_type, "_mget"), params=params, body=body
        )