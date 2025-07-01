def register(self, params, target):
        """Expect observation with known target"""
        self._space.register(params, target)
        self.dispatch(Events.OPTMIZATION_STEP)