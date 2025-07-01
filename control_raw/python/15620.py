def get_library_meta(self):
        '''
        Fetches the meta data for the current library. The data could be in
        the superlib meta data file. If we can't find the data None is returned.
        '''
        parent_dir = os.path.dirname(self.library_dir)
        if self.test_file_exists(os.path.join(self.library_dir,'meta'),['libraries.json']):
            with open(os.path.join(self.library_dir,'meta','libraries.json'),'r') as f:
                meta_data = json.load(f)
                if isinstance(meta_data,list):
                    for lib in meta_data:
                        if lib['key'] == self.library_key:
                            return lib
                elif 'key' in meta_data and meta_data['key'] == self.library_key:
                    return meta_data
        if not self.test_dir_exists(os.path.join(self.library_dir,'meta')) \
            and self.test_file_exists(os.path.join(parent_dir,'meta'),['libraries.json']):
            with open(os.path.join(parent_dir,'meta','libraries.json'),'r') as f:
                libraries_json = json.load(f)
                if isinstance(libraries_json,list):
                    for lib in libraries_json:
                        if lib['key'] == self.library_key:
                            return lib
        return None