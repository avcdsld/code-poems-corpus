def _load_class_names(self, filename, dirname):
        """
        load class names from text file

        Parameters:
        ----------
        filename: str
            file stores class names
        dirname: str
            file directory
        """
        full_path = osp.join(dirname, filename)
        classes = []
        with open(full_path, 'r') as f:
            classes = [l.strip() for l in f.readlines()]
        return classes