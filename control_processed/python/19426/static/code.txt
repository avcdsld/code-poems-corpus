def create_process_worker(self, cmd_list, environ=None):
        """Create a new process worker instance."""
        worker = ProcessWorker(cmd_list, environ=environ)
        self._create_worker(worker)
        return worker