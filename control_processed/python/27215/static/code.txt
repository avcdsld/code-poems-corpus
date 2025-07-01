def ret_pcre_minions(self):
        '''
        Return minions that match via pcre
        '''
        tgt = re.compile(self.tgt)
        refilter = functools.partial(filter, tgt.match)
        return self._ret_minions(refilter)