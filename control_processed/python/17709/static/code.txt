def is_valid(self):
        """
        Runs the SAM Translator to determine if the template provided is valid. This is similar to running a
        ChangeSet in CloudFormation for a SAM Template

        Raises
        -------
        InvalidSamDocumentException
             If the template is not valid, an InvalidSamDocumentException is raised
        """
        managed_policy_map = self.managed_policy_loader.load()

        sam_translator = Translator(managed_policy_map=managed_policy_map,
                                    sam_parser=self.sam_parser,
                                    plugins=[])

        self._replace_local_codeuri()

        try:
            template = sam_translator.translate(sam_template=self.sam_template,
                                                parameter_values={})
            LOG.debug("Translated template is:\n%s", yaml_dump(template))
        except InvalidDocumentException as e:
            raise InvalidSamDocumentException(
                functools.reduce(lambda message, error: message + ' ' + str(error), e.causes, str(e)))