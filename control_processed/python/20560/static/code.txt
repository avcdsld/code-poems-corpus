def mkdir(self, path, parents=True, mode=0o755, raise_if_exists=False):
        """
        Has no returnvalue (just like WebHDFS)
        """
        if not parents or raise_if_exists:
            warnings.warn('webhdfs mkdir: parents/raise_if_exists not implemented')
        permission = int(oct(mode)[2:])  # Convert from int(decimal) to int(octal)
        self.client.makedirs(path, permission=permission)