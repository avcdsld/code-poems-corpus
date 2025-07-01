def cache_file(self, template):
        '''
        Cache a file from the salt master
        '''
        saltpath = salt.utils.url.create(template)
        self.file_client().get_file(saltpath, '', True, self.saltenv)