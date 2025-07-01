def webui_url(args):
    '''show the url of web ui'''
    nni_config = Config(get_config_filename(args))
    print_normal('{0} {1}'.format('Web UI url:', ' '.join(nni_config.get_config('webuiUrl'))))