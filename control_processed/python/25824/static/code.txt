def local_async(self, *args, **kwargs):
        '''
        Run :ref:`execution modules <all-salt.modules>` asynchronously

        Wraps :py:meth:`salt.client.LocalClient.run_job`.

        :return: job ID
        '''
        local = salt.client.get_local_client(mopts=self.opts)
        ret = local.run_job(*args, **kwargs)
        return ret