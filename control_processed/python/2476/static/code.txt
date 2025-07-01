def steps(self, *steps_cfg:StartOptEnd):
        "Build anneal schedule for all of the parameters."
        return [Scheduler(step, n_iter, func=func)
                for (step,(n_iter,func)) in zip(steps_cfg, self.phases)]