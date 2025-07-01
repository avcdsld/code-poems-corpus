def expand_parameters(self, para):
        '''
        Enumerate all possible combinations of all parameters
        para: {key1: [v11, v12, ...], key2: [v21, v22, ...], ...}
        return: {{key1: v11, key2: v21, ...}, {key1: v11, key2: v22, ...}, ...}
        '''
        if len(para) == 1:
            for key, values in para.items():
                return list(map(lambda v: {key: v}, values))

        key = list(para)[0]
        values = para.pop(key)
        rest_para = self.expand_parameters(para)
        ret_para = list()
        for val in values:
            for config in rest_para:
                config[key] = val
                ret_para.append(copy.deepcopy(config))
        return ret_para