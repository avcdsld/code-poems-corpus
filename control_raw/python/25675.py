def connect(connect_spec=None):
    '''Connect and optionally bind to an LDAP server.

    :param connect_spec:
        This can be an LDAP connection object returned by a previous
        call to :py:func:`connect` (in which case the argument is
        simply returned), ``None`` (in which case an empty dict is
        used), or a dict with the following keys:

        * ``'backend'``
            Optional; default depends on which Python LDAP modules are
            installed.  Name of the Python LDAP module to use.  Only
            ``'ldap'`` is supported at the moment.

        * ``'url'``
            Optional; defaults to ``'ldapi:///'``.  URL to the LDAP
            server.

        * ``'bind'``
            Optional; defaults to ``None``.  Describes how to bind an
            identity to the LDAP connection.  If ``None``, an
            anonymous connection is made.  Valid keys:

            * ``'method'``
                Optional; defaults to ``None``.  The authentication
                method to use.  Valid values include but are not
                necessarily limited to ``'simple'``, ``'sasl'``, and
                ``None``.  If ``None``, an anonymous connection is
                made.  Available methods depend on the chosen backend.

            * ``'mechanism'``
                Optional; defaults to ``'EXTERNAL'``.  The SASL
                mechanism to use.  Ignored unless the method is
                ``'sasl'``.  Available methods depend on the chosen
                backend and the server's capabilities.

            * ``'credentials'``
                Optional; defaults to ``None``.  An object specific to
                the chosen SASL mechanism and backend that represents
                the authentication credentials.  Ignored unless the
                method is ``'sasl'``.

                For the ``'ldap'`` backend, this is a dictionary.  If
                ``None``, an empty dict is used.  Keys:

                * ``'args'``
                    Optional; defaults to an empty list.  A list of
                    arguments to pass to the SASL mechanism
                    constructor.  See the SASL mechanism constructor
                    documentation in the ``ldap.sasl`` Python module.

                * ``'kwargs'``
                    Optional; defaults to an empty dict.  A dict of
                    keyword arguments to pass to the SASL mechanism
                    constructor.  See the SASL mechanism constructor
                    documentation in the ``ldap.sasl`` Python module.

            * ``'dn'``
                Optional; defaults to an empty string.  The
                distinguished name to bind.

            * ``'password'``
                Optional; defaults to an empty string.  Password for
                binding.  Ignored if the method is ``'sasl'``.

        * ``'tls'``
            Optional; defaults to ``None``.  A backend-specific object
            containing settings to override default TLS behavior.

            For the ``'ldap'`` backend, this is a dictionary.  Not all
            settings in this dictionary are supported by all versions
            of ``python-ldap`` or the underlying TLS library.  If
            ``None``, an empty dict is used.  Possible keys:

            * ``'starttls'``
                If present, initiate a TLS connection using StartTLS.
                (The value associated with this key is ignored.)

            * ``'cacertdir'``
                Set the path of the directory containing CA
                certificates.

            * ``'cacertfile'``
                Set the pathname of the CA certificate file.

            * ``'certfile'``
                Set the pathname of the certificate file.

            * ``'cipher_suite'``
                Set the allowed cipher suite.

            * ``'crlcheck'``
                Set the CRL evaluation strategy.  Valid values are
                ``'none'``, ``'peer'``, and ``'all'``.

            * ``'crlfile'``
                Set the pathname of the CRL file.

            * ``'dhfile'``
                Set the pathname of the file containing the parameters
                for Diffie-Hellman ephemeral key exchange.

            * ``'keyfile'``
                Set the pathname of the certificate key file.

            * ``'newctx'``
                If present, instruct the underlying TLS library to
                create a new TLS context.  (The value associated with
                this key is ignored.)

            * ``'protocol_min'``
                Set the minimum protocol version.

            * ``'random_file'``
                Set the pathname of the random file when
                ``/dev/random`` and ``/dev/urandom`` are not
                available.

            * ``'require_cert'``
                Set the certificate validation policy.  Valid values
                are ``'never'``, ``'hard'``, ``'demand'``,
                ``'allow'``, and ``'try'``.

        * ``'opts'``
            Optional; defaults to ``None``.  A backend-specific object
            containing options for the backend.

            For the ``'ldap'`` backend, this is a dictionary of
            OpenLDAP options to set.  If ``None``, an empty dict is
            used.  Each key is a the name of an OpenLDAP option
            constant without the ``'LDAP_OPT_'`` prefix, then
            converted to lower case.

    :returns:
        an object representing an LDAP connection that can be used as
        the ``connect_spec`` argument to any of the functions in this
        module (to avoid the overhead of making and terminating
        multiple connections).

        This object should be used as a context manager.  It is safe
        to nest ``with`` statements.

    CLI example:

    .. code-block:: bash

        salt '*' ldap3.connect "{
            'url': 'ldaps://ldap.example.com/',
            'bind': {
                'method': 'simple',
                'dn': 'cn=admin,dc=example,dc=com',
                'password': 'secret'}
        }"
    '''
    if isinstance(connect_spec, _connect_ctx):
        return connect_spec
    if connect_spec is None:
        connect_spec = {}
    backend_name = connect_spec.get('backend', 'ldap')
    if backend_name not in available_backends:
        raise ValueError('unsupported backend or required Python module'
                         + ' unavailable: {0}'.format(backend_name))
    url = connect_spec.get('url', 'ldapi:///')
    try:
        l = ldap.initialize(url)
        l.protocol_version = ldap.VERSION3

        # set up tls
        tls = connect_spec.get('tls', None)
        if tls is None:
            tls = {}
        vars = {}
        for k, v in six.iteritems(tls):
            if k in ('starttls', 'newctx'):
                vars[k] = True
            elif k in ('crlcheck', 'require_cert'):
                l.set_option(getattr(ldap, 'OPT_X_TLS_' + k.upper()),
                             getattr(ldap, 'OPT_X_TLS_' + v.upper()))
            else:
                l.set_option(getattr(ldap, 'OPT_X_TLS_' + k.upper()), v)
        if vars.get('starttls', False):
            l.start_tls_s()
        if vars.get('newctx', False):
            l.set_option(ldap.OPT_X_TLS_NEWCTX, 0)

        # set up other options
        l.set_option(ldap.OPT_REFERRALS, 0)
        opts = connect_spec.get('opts', None)
        if opts is None:
            opts = {}
        for k, v in six.iteritems(opts):
            opt = getattr(ldap, 'OPT_' + k.upper())
            l.set_option(opt, v)

        _bind(l, connect_spec.get('bind', None))
    except ldap.LDAPError as e:
        _convert_exception(e)
    return _connect_ctx(l)