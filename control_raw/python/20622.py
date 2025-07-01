def do_prune(self):
        """
        Return True if prune_table, prune_column, and prune_date are implemented.
        If only a subset of prune variables are override, an exception is raised to remind the user to implement all or none.
        Prune (data newer than prune_date deleted) before copying new data in.
        """
        if self.prune_table and self.prune_column and self.prune_date:
            return True
        elif self.prune_table or self.prune_column or self.prune_date:
            raise Exception('override zero or all prune variables')
        else:
            return False