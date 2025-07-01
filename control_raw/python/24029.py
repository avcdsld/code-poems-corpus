def start():
    '''
    Start the server loop
    '''
    from . import app
    root, apiopts, conf = app.get_app(__opts__)

    if not apiopts.get('disable_ssl', False):
        if 'ssl_crt' not in apiopts or 'ssl_key' not in apiopts:
            logger.error("Not starting '%s'. Options 'ssl_crt' and "
                    "'ssl_key' are required if SSL is not disabled.",
                    __name__)

            return None

        verify_certs(apiopts['ssl_crt'], apiopts['ssl_key'])

        cherrypy.server.ssl_module = 'builtin'
        cherrypy.server.ssl_certificate = apiopts['ssl_crt']
        cherrypy.server.ssl_private_key = apiopts['ssl_key']
        if 'ssl_chain' in apiopts.keys():
            cherrypy.server.ssl_certificate_chain = apiopts['ssl_chain']

    cherrypy.quickstart(root, apiopts.get('root_prefix', '/'), conf)