def _parameter_objects(parameter_objects_from_pillars, parameter_object_overrides):
    '''
    Return a list of parameter objects that configure the pipeline

    parameter_objects_from_pillars
        The pillar key to use for lookup

    parameter_object_overrides
        Parameter objects to use. Will override objects read from pillars.
    '''
    from_pillars = copy.deepcopy(__salt__['pillar.get'](parameter_objects_from_pillars))
    from_pillars.update(parameter_object_overrides)
    parameter_objects = _standardize(_dict_to_list_ids(from_pillars))
    for parameter_object in parameter_objects:
        parameter_object['attributes'] = _properties_from_dict(parameter_object['attributes'])
    return parameter_objects