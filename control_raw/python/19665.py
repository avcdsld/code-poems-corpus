def load_history(self):
        """Load history from a .py file in user home directory"""
        if osp.isfile(self.history_filename):
            rawhistory, _ = encoding.readlines(self.history_filename)
            rawhistory = [line.replace('\n', '') for line in rawhistory]
            if rawhistory[1] != self.INITHISTORY[1]:
                rawhistory[1] = self.INITHISTORY[1]
        else:
            rawhistory = self.INITHISTORY
        history = [line for line in rawhistory \
                   if line and not line.startswith('#')]

        # Truncating history to X entries:
        while len(history) >= CONF.get('historylog', 'max_entries'):
            del history[0]
            while rawhistory[0].startswith('#'):
                del rawhistory[0]
            del rawhistory[0]

        # Saving truncated history:
        try:
            encoding.writelines(rawhistory, self.history_filename)
        except EnvironmentError:
            pass

        return history