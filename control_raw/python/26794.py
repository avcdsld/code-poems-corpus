def absent(name):
    '''
    Ensure that the named index is absent.

    name
        Name of the index to remove
    '''

    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}

    try:
        index = __salt__['elasticsearch.index_get'](index=name)
        if index and name in index:
            if __opts__['test']:
                ret['comment'] = 'Index {0} will be removed'.format(name)
                ret['changes']['old'] = index[name]
                ret['result'] = None
            else:
                ret['result'] = __salt__['elasticsearch.index_delete'](index=name)
                if ret['result']:
                    ret['comment'] = 'Successfully removed index {0}'.format(name)
                    ret['changes']['old'] = index[name]
                else:
                    ret['comment'] = 'Failed to remove index {0} for unknown reasons'.format(name)
        else:
            ret['comment'] = 'Index {0} is already absent'.format(name)
    except Exception as err:
        ret['result'] = False
        ret['comment'] = six.text_type(err)

    return ret