def pipeline_absent(name):
    '''
    Ensure that the named pipeline is absent

    name
        Name of the pipeline to remove
    '''

    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}

    try:
        pipeline = __salt__['elasticsearch.pipeline_get'](id=name)
        if pipeline and name in pipeline:
            if __opts__['test']:
                ret['comment'] = 'Pipeline {0} will be removed'.format(name)
                ret['changes']['old'] = pipeline[name]
                ret['result'] = None
            else:
                ret['result'] = __salt__['elasticsearch.pipeline_delete'](id=name)
                if ret['result']:
                    ret['comment'] = 'Successfully removed pipeline {0}'.format(name)
                    ret['changes']['old'] = pipeline[name]
                else:
                    ret['comment'] = 'Failed to remove pipeline {0} for unknown reasons'.format(name)
        else:
            ret['comment'] = 'Pipeline {0} is already absent'.format(name)
    except Exception as err:
        ret['result'] = False
        ret['comment'] = six.text_type(err)

    return ret