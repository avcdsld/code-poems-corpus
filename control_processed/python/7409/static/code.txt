def tic(self):
        """Start collecting stats for current batch.
        Call before calling forward."""
        if self.step % self.interval == 0:
            for exe in self.exes:
                for array in exe.arg_arrays:
                    array.wait_to_read()
                for array in exe.aux_arrays:
                    array.wait_to_read()
            self.queue = []
            self.activated = True
        self.step += 1