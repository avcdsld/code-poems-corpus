def supported(self, tags=None):
        # type: (Optional[List[Pep425Tag]]) -> bool
        """Is this wheel supported on this system?"""
        if tags is None:  # for mock
            tags = pep425tags.get_supported()
        return bool(set(tags).intersection(self.file_tags))