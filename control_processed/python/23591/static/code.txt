def provider_list(self, lookup='all'):
        '''
        Return a mapping of all image data for available providers
        '''
        data = {}
        lookups = self.lookup_providers(lookup)
        if not lookups:
            return data

        for alias, driver in lookups:
            if alias not in data:
                data[alias] = {}
            if driver not in data[alias]:
                data[alias][driver] = {}
        return data