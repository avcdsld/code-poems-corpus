def cmd(self,
            tgt,
            fun,
            arg=(),
            timeout=None,
            tgt_type='glob',
            kwarg=None,
            **kwargs):
        '''
        Execute a single command via the salt-ssh subsystem and return all
        routines at once

        .. versionadded:: 2015.5.0
        '''
        ssh = self._prep_ssh(
                tgt,
                fun,
                arg,
                timeout,
                tgt_type,
                kwarg,
                **kwargs)
        final = {}
        for ret in ssh.run_iter(jid=kwargs.get('jid', None)):
            final.update(ret)
        return final