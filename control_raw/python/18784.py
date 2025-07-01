def get(self, name_or_klass):
        """
        Gets a specific panel instance.

        :param name_or_klass: Name or class of the panel to retrieve.
        :return: The specified panel instance.
        """
        if not is_text_string(name_or_klass):
            name_or_klass = name_or_klass.__name__
        for zone in range(4):
            try:
                panel = self._panels[zone][name_or_klass]
            except KeyError:
                pass
            else:
                return panel
        raise KeyError(name_or_klass)