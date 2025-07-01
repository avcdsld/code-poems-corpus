def render(template, saltenv='base', sls='', tmplpath=None, **kws):
    '''
    Render the python module's components

    :rtype: string
    '''
    template = tmplpath
    if not os.path.isfile(template):
        raise SaltRenderError('Template {0} is not a file!'.format(template))

    tmp_data = salt.utils.templates.py(
            template,
            True,
            __salt__=__salt__,
            salt=__salt__,
            __grains__=__grains__,
            grains=__grains__,
            __opts__=__opts__,
            opts=__opts__,
            __pillar__=__pillar__,
            pillar=__pillar__,
            __env__=saltenv,
            saltenv=saltenv,
            __sls__=sls,
            sls=sls,
            **kws)
    if not tmp_data.get('result', False):
        raise SaltRenderError(tmp_data.get('data',
            'Unknown render error in py renderer'))

    return tmp_data['data']