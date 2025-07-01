def _check_source(cls, source_file_hash, source):
        """Checks if a pre-trained token embedding source name is valid.


        Parameters
        ----------
        source : str
            The pre-trained token embedding source.
        """
        embedding_name = cls.__name__.lower()
        if source not in source_file_hash:
            raise KeyError('Cannot find pre-trained source {} for token embedding {}. '
                           'Valid pre-trained file names for embedding {}: {}'.format(
                               source, embedding_name, embedding_name,
                               ', '.join(source_file_hash.keys())))