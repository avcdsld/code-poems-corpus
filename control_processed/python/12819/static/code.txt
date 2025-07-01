def mutation(self, config=None, info=None, save_dir=None):
        """
        Parameters
        ----------
        config : str
        info : str
        save_dir : str
        """
        self.result = None
        self.config = config
        self.restore_dir = self.save_dir
        self.save_dir = save_dir
        self.info = info