def get_cache_key(self, name, filename=None):
        """Returns the unique hash key for this template name."""
        hash = sha1(name.encode('utf-8'))
        if filename is not None:
            filename = '|' + filename
            if isinstance(filename, text_type):
                filename = filename.encode('utf-8')
            hash.update(filename)
        return hash.hexdigest()