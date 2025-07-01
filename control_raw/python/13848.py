def save_predefined(self, predefined, client=None):
        """Save this ACL for the current bucket using a predefined ACL.

        If :attr:`user_project` is set, bills the API request to that project.

        :type predefined: str
        :param predefined: An identifier for a predefined ACL.  Must be one
                           of the keys in :attr:`PREDEFINED_JSON_ACLS`
                           or :attr:`PREDEFINED_XML_ACLS` (which will be
                           aliased to the corresponding JSON name).
                           If passed, `acl` must be None.

        :type client: :class:`~google.cloud.storage.client.Client` or
                      ``NoneType``
        :param client: Optional. The client to use.  If not passed, falls back
                       to the ``client`` stored on the ACL's parent.
        """
        predefined = self.validate_predefined(predefined)
        self._save(None, predefined, client)