def cache_response(self, request, response, body=None, status_codes=None):
        """
        Algorithm for caching requests.

        This assumes a requests Response object.
        """
        # From httplib2: Don't cache 206's since we aren't going to
        #                handle byte range requests
        cacheable_status_codes = status_codes or self.cacheable_status_codes
        if response.status not in cacheable_status_codes:
            logger.debug(
                "Status code %s not in %s", response.status, cacheable_status_codes
            )
            return

        response_headers = CaseInsensitiveDict(response.headers)

        # If we've been given a body, our response has a Content-Length, that
        # Content-Length is valid then we can check to see if the body we've
        # been given matches the expected size, and if it doesn't we'll just
        # skip trying to cache it.
        if (
            body is not None
            and "content-length" in response_headers
            and response_headers["content-length"].isdigit()
            and int(response_headers["content-length"]) != len(body)
        ):
            return

        cc_req = self.parse_cache_control(request.headers)
        cc = self.parse_cache_control(response_headers)

        cache_url = self.cache_url(request.url)
        logger.debug('Updating cache with response from "%s"', cache_url)

        # Delete it from the cache if we happen to have it stored there
        no_store = False
        if "no-store" in cc:
            no_store = True
            logger.debug('Response header has "no-store"')
        if "no-store" in cc_req:
            no_store = True
            logger.debug('Request header has "no-store"')
        if no_store and self.cache.get(cache_url):
            logger.debug('Purging existing cache entry to honor "no-store"')
            self.cache.delete(cache_url)
        if no_store:
            return

        # If we've been given an etag, then keep the response
        if self.cache_etags and "etag" in response_headers:
            logger.debug("Caching due to etag")
            self.cache.set(
                cache_url, self.serializer.dumps(request, response, body=body)
            )

        # Add to the cache any 301s. We do this before looking that
        # the Date headers.
        elif response.status == 301:
            logger.debug("Caching permanant redirect")
            self.cache.set(cache_url, self.serializer.dumps(request, response))

        # Add to the cache if the response headers demand it. If there
        # is no date header then we can't do anything about expiring
        # the cache.
        elif "date" in response_headers:
            # cache when there is a max-age > 0
            if "max-age" in cc and cc["max-age"] > 0:
                logger.debug("Caching b/c date exists and max-age > 0")
                self.cache.set(
                    cache_url, self.serializer.dumps(request, response, body=body)
                )

            # If the request can expire, it means we should cache it
            # in the meantime.
            elif "expires" in response_headers:
                if response_headers["expires"]:
                    logger.debug("Caching b/c of expires header")
                    self.cache.set(
                        cache_url, self.serializer.dumps(request, response, body=body)
                    )