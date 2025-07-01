def get_errors(self):
        """
        Return any errors which have occurred.
        """
        result = []
        while not self.errors.empty():  # pragma: no cover
            try:
                e = self.errors.get(False)
                result.append(e)
            except self.errors.Empty:
                continue
            self.errors.task_done()
        return result