def get_exception(self):
        """
        Return any exception that happened during the last server request.
        This can be used to fetch more specific error information after using
        calls like `start_client`.  The exception (if any) is cleared after
        this call.

        :return:
            an exception, or ``None`` if there is no stored exception.

        .. versionadded:: 1.1
        """
        self.lock.acquire()
        try:
            e = self.saved_exception
            self.saved_exception = None
            return e
        finally:
            self.lock.release()