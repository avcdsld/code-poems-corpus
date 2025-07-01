def run(self):
        """
        The execution of this task will write 4 lines of data on this task's target output.
        """
        with self.output().open('w') as outfile:
            print("data 0 200 10 50 60", file=outfile)
            print("data 1 190 9 52 60", file=outfile)
            print("data 2 200 10 52 60", file=outfile)
            print("data 3 195 1 52 60", file=outfile)