def _get_os(self):
        '''
        Get operating system summary
        '''
        return {
            'name': self._grain('os'),
            'family': self._grain('os_family'),
            'arch': self._grain('osarch'),
            'release': self._grain('osrelease'),
        }