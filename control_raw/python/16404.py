def get(self, id, param):
        """ Returns the value of a configuration parameter. """
        assert isinstance(id, basestring)
        assert isinstance(param, basestring)
        return self.params_.get(param, {}).get(id)