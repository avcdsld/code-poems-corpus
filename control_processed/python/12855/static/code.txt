def get_all_config(self):
        '''get all of config values'''
        return json.dumps(self.config, indent=4, sort_keys=True, separators=(',', ':'))