def get_application(*args):
    '''
    Returns a WSGI application function. If you supply the WSGI app and config
    it will use that, otherwise it will try to obtain them from a local Salt
    installation
    '''
    opts_tuple = args

    def wsgi_app(environ, start_response):
        root, _, conf = opts_tuple or bootstrap_app()
        cherrypy.config.update({'environment': 'embedded'})

        cherrypy.tree.mount(root, '/', conf)
        return cherrypy.tree(environ, start_response)

    return wsgi_app