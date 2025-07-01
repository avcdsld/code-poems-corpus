def rename_dont_move(self, path, dest):
        """
        Use snakebite.rename_dont_move, if available.

        :param path: source path (single input)
        :type path: string
        :param dest: destination path
        :type dest: string
        :return: True if succeeded
        :raises: snakebite.errors.FileAlreadyExistsException
        """
        from snakebite.errors import FileAlreadyExistsException
        try:
            self.get_bite().rename2(path, dest, overwriteDest=False)
        except FileAlreadyExistsException:
            # Unfortunately python2 don't allow exception chaining.
            raise luigi.target.FileAlreadyExists()