def targets(self, tgt, tgt_type):
        '''
        Return a dict of {'id': {'ipv4': <ipaddr>}} data sets to be used as
        targets given the passed tgt and tgt_type
        '''
        targets = {}
        for back in self._gen_back():
            f_str = '{0}.targets'.format(back)
            if f_str not in self.rosters:
                continue
            try:
                targets.update(self.rosters[f_str](tgt, tgt_type))
            except salt.exceptions.SaltRenderError as exc:
                log.error('Unable to render roster file: %s', exc)
            except IOError as exc:
                log.error("Can't access roster for backend %s: %s", back, exc)

        log.debug('Matched minions: %s', targets)
        return targets