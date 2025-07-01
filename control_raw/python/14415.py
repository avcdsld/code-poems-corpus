def get_languages(self, target_language=None):
        """Get list of supported languages for translation.

        Response

        See
        https://cloud.google.com/translate/docs/discovering-supported-languages

        :type target_language: str
        :param target_language: (Optional) The language used to localize
                                returned language names. Defaults to the
                                target language on the current client.

        :rtype: list
        :returns: List of dictionaries. Each dictionary contains a supported
                  ISO 639-1 language code (using the dictionary key
                  ``language``). If ``target_language`` is passed, each
                  dictionary will also contain the name of each supported
                  language (localized to the target language).
        """
        query_params = {}
        if target_language is None:
            target_language = self.target_language
        if target_language is not None:
            query_params["target"] = target_language
        response = self._connection.api_request(
            method="GET", path="/languages", query_params=query_params
        )
        return response.get("data", {}).get("languages", ())