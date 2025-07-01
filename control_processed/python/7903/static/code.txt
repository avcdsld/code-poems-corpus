def iter_next(self):
        """Increments the coursor by batch_size for next batch
        and check current cursor if it exceed the number of data points."""
        self.cursor += self.batch_size
        return self.cursor < self.num_data