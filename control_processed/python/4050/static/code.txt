def fetch2(self, path, api='public', method='GET', params={}, headers=None, body=None):
        """A better wrapper over request for deferred signing"""
        if self.enableRateLimit:
            self.throttle()
        self.lastRestRequestTimestamp = self.milliseconds()
        request = self.sign(path, api, method, params, headers, body)
        return self.fetch(request['url'], request['method'], request['headers'], request['body'])