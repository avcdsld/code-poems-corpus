def schemaSetValidOptions(self, options):
        """Sets the options to be used during the validation. """
        ret = libxml2mod.xmlSchemaSetValidOptions(self._o, options)
        return ret