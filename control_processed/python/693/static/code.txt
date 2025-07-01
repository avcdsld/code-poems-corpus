def textFileStream(self, directory):
        """
        Create an input stream that monitors a Hadoop-compatible file system
        for new files and reads them as text files. Files must be wrriten to the
        monitored directory by "moving" them from another location within the same
        file system. File names starting with . are ignored.
        The text files must be encoded as UTF-8.
        """
        return DStream(self._jssc.textFileStream(directory), self, UTF8Deserializer())