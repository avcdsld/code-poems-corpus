def _read_from_definition_body(self):
        """
        Read the Swagger document from DefinitionBody. It could either be an inline Swagger dictionary or an
        AWS::Include macro that contains location of the included Swagger. In the later case, we will download and
        parse the Swagger document.

        Returns
        -------
        dict
            Swagger document, if we were able to parse. None, otherwise
        """

        # Let's try to parse it as AWS::Include Transform first. If not, then fall back to assuming the Swagger document
        # was inclined directly into the body
        location = parse_aws_include_transform(self.definition_body)
        if location:
            LOG.debug("Trying to download Swagger from %s", location)
            return self._download_swagger(location)

        # Inline Swagger, just return the contents which should already be a dictionary
        LOG.debug("Detected Inline Swagger definition")
        return self.definition_body