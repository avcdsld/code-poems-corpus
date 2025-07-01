def cache_param(self, value):
        '''Returns a troposphere Ref to a value cached as a parameter.'''

        if value not in self.cf_parameters:
            keyname = chr(ord('A') + len(self.cf_parameters))
            param = self.cf_template.add_parameter(troposphere.Parameter(
                keyname, Type="String", Default=value, tags=self.tags
            ))

            self.cf_parameters[value] = param

        return troposphere.Ref(self.cf_parameters[value])