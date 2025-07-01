def pillars(opts, functions, context=None):
    '''
    Returns the pillars modules
    '''
    ret = LazyLoader(_module_dirs(opts, 'pillar'),
                     opts,
                     tag='pillar',
                     pack={'__salt__': functions,
                           '__context__': context,
                           '__utils__': utils(opts)})
    ret.pack['__ext_pillar__'] = ret
    return FilterDictWrapper(ret, '.ext_pillar')