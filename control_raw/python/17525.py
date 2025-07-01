def phantomjs_fetch(self, url, task):
        '''Fetch with phantomjs proxy'''
        start_time = time.time()
        self.on_fetch('phantomjs', task)
        handle_error = lambda x: self.handle_error('phantomjs', url, task, start_time, x)

        # check phantomjs proxy is enabled
        if not self.phantomjs_proxy:
            result = {
                "orig_url": url,
                "content": "phantomjs is not enabled.",
                "headers": {},
                "status_code": 501,
                "url": url,
                "time": time.time() - start_time,
                "cookies": {},
                "save": task.get('fetch', {}).get('save')
            }
            logger.warning("[501] %s:%s %s 0s", task.get('project'), task.get('taskid'), url)
            raise gen.Return(result)

        # setup request parameters
        fetch = self.pack_tornado_request_parameters(url, task)
        task_fetch = task.get('fetch', {})
        for each in task_fetch:
            if each not in fetch:
                fetch[each] = task_fetch[each]

        # robots.txt
        if task_fetch.get('robots_txt', False):
            user_agent = fetch['headers']['User-Agent']
            can_fetch = yield self.can_fetch(user_agent, url)
            if not can_fetch:
                error = tornado.httpclient.HTTPError(403, 'Disallowed by robots.txt')
                raise gen.Return(handle_error(error))

        request_conf = {
            'follow_redirects': False
        }
        request_conf['connect_timeout'] = fetch.get('connect_timeout', 20)
        request_conf['request_timeout'] = fetch.get('request_timeout', 120) + 1

        session = cookies.RequestsCookieJar()
        if 'Cookie' in fetch['headers']:
            c = http_cookies.SimpleCookie()
            try:
                c.load(fetch['headers']['Cookie'])
            except AttributeError:
                c.load(utils.utf8(fetch['headers']['Cookie']))
            for key in c:
                session.set(key, c[key])
            del fetch['headers']['Cookie']
        if 'cookies' in fetch:
            session.update(fetch['cookies'])
            del fetch['cookies']

        request = tornado.httpclient.HTTPRequest(url=fetch['url'])
        cookie_header = cookies.get_cookie_header(session, request)
        if cookie_header:
            fetch['headers']['Cookie'] = cookie_header

        # making requests
        fetch['headers'] = dict(fetch['headers'])
        try:
            request = tornado.httpclient.HTTPRequest(
                url=self.phantomjs_proxy, method="POST",
                body=json.dumps(fetch), **request_conf)
        except Exception as e:
            raise gen.Return(handle_error(e))

        try:
            response = yield gen.maybe_future(self.http_client.fetch(request))
        except tornado.httpclient.HTTPError as e:
            if e.response:
                response = e.response
            else:
                raise gen.Return(handle_error(e))

        if not response.body:
            raise gen.Return(handle_error(Exception('no response from phantomjs: %r' % response)))

        result = {}
        try:
            result = json.loads(utils.text(response.body))
            assert 'status_code' in result, result
        except Exception as e:
            if response.error:
                result['error'] = utils.text(response.error)
            raise gen.Return(handle_error(e))

        if result.get('status_code', 200):
            logger.info("[%d] %s:%s %s %.2fs", result['status_code'],
                        task.get('project'), task.get('taskid'), url, result['time'])
        else:
            logger.error("[%d] %s:%s %s, %r %.2fs", result['status_code'],
                         task.get('project'), task.get('taskid'),
                         url, result['content'], result['time'])

        raise gen.Return(result)