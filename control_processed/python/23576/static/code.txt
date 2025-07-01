def list_locations(self, provider=None):
        '''
        List all available locations in configured cloud systems
        '''
        mapper = salt.cloud.Map(self._opts_defaults())
        return salt.utils.data.simple_types_filter(
            mapper.location_list(provider)
        )