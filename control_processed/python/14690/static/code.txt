def sink_get(self, project, sink_name):
        """API call:  retrieve a sink resource.

        See
        https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks/get

        :type project: str
        :param project: ID of the project containing the sink.

        :type sink_name: str
        :param sink_name: the name of the sink

        :rtype: dict
        :returns: The JSON sink object returned from the API.
        """
        target = "/projects/%s/sinks/%s" % (project, sink_name)
        return self.api_request(method="GET", path=target)