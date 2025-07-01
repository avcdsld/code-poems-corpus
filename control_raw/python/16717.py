def xincludeProcessFlags(self, flags):
        """Implement the XInclude substitution on the XML document @doc """
        ret = libxml2mod.xmlXIncludeProcessFlags(self._o, flags)
        return ret