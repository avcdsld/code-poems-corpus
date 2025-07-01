function (request, defaultOpts, protocolProfileBehavior) {
        var options = {},
            networkOptions = defaultOpts.network || {},
            self = this,
            bodyParams,
            url = request.url && urlEncoder.toNodeUrl(request.url.toString(true)),
            isSSL,
            reqOption,
            portNumber,
            behaviorName,
            port = url && url.port,
            hostname = url && url.hostname;

        !defaultOpts && (defaultOpts = {});
        !protocolProfileBehavior && (protocolProfileBehavior = {});

        options.url = url;
        options.method = request.method;
        options.jar = defaultOpts.cookieJar || true;
        options.timeout = defaultOpts.timeout;
        options.gzip = true;
        options.time = defaultOpts.timings;
        options.verbose = defaultOpts.verbose;
        options.extraCA = defaultOpts.extendedRootCA;

        // Disable encoding of URL in postman-request in order to use pre-encoded URL object returned from
        // toNodeUrl() function of postman-url-encoder
        options.disableUrlEncoding = true;

        // Ensures that "request" creates URL encoded formdata or querystring as
        // foo=bar&foo=baz instead of foo[0]=bar&foo[1]=baz
        options.useQuerystring = true;

        // set encoding to null so that the response is a stream
        options.encoding = null;

        // eslint-disable-next-line guard-for-in
        for (reqOption in PPB_OPTS) {
            behaviorName = PPB_OPTS[reqOption];
            options[reqOption] = resolveWithProtocolProfileBehavior(behaviorName, defaultOpts, protocolProfileBehavior);
        }

        // use the server's cipher suite order instead of the client's during negotiation
        if (protocolProfileBehavior.tlsPreferServerCiphers) {
            options.honorCipherOrder = true;
        }

        // the SSL and TLS protocol versions to disabled during negotiation
        if (Array.isArray(protocolProfileBehavior.tlsDisabledProtocols)) {
            protocolProfileBehavior.tlsDisabledProtocols.forEach(function (protocol) {
                options.secureOptions |= constants[SSL_OP_NO + protocol];
            });
        }

        // order of cipher suites that the SSL server profile uses to establish a secure connection
        if (Array.isArray(protocolProfileBehavior.tlsCipherSelection)) {
            options.ciphers = protocolProfileBehavior.tlsCipherSelection.join(':');
        }

        // Request body may return different options depending on the type of the body.
        bodyParams = self.getRequestBody(request, protocolProfileBehavior);

        // @note getRequestBody may add system headers based on intent
        options.headers = request.getHeaders({enabled: true, sanitizeKeys: true});

        // Insert any headers that XHR inserts, to keep the Node version compatible with the Chrome App
        if (bodyParams && bodyParams.body) {
            self.ensureHeaderExists(options.headers, 'Content-Type', 'text/plain');
        }
        self.ensureHeaderExists(options.headers, 'User-Agent', 'PostmanRuntime/' + version);
        self.ensureHeaderExists(options.headers, 'Accept', '*/*');

        defaultOpts.implicitCacheControl && self.ensureHeaderExists(options.headers, 'Cache-Control', 'no-cache');
        // @todo avoid invoking uuid() if header exists
        defaultOpts.implicitTraceHeader && self.ensureHeaderExists(options.headers, 'Postman-Token', uuid());

        // The underlying Node client does add the host header by itself, but we add it anyway, so that
        // it is bubbled up to us after the request is made. If left to the underlying core, it's not :/
        self.ensureHeaderExists(options.headers, 'Host', url.host);

        // override DNS lookup
        if (networkOptions.restrictedAddresses || hostname.toLowerCase() === LOCALHOST || networkOptions.hostLookup) {
            isSSL = _.startsWith(request.url.protocol, HTTPS);
            portNumber = Number(port) || (isSSL ? HTTPS_DEFAULT_PORT : HTTP_DEFAULT_PORT);

            _.isFinite(portNumber) && (options.lookup = lookup.bind(this, {
                port: portNumber,
                network: networkOptions
            }));
        }

        _.assign(options, bodyParams, {
            agentOptions: {
                keepAlive: defaultOpts.keepAlive
            }
        });

        return options;
    }