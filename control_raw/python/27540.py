def runner(self, fun, **kwargs):
        '''
        Wrap RunnerClient for executing :ref:`runner modules <all-salt.runners>`
        '''
        return self.pool.fire_async(self.client_cache['runner'].low, args=(fun, kwargs))