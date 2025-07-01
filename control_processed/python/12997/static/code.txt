def set_experiment(experiment_config, mode, port, config_file_name):
    '''Call startExperiment (rest POST /experiment) with yaml file content'''
    request_data = dict()
    request_data['authorName'] = experiment_config['authorName']
    request_data['experimentName'] = experiment_config['experimentName']
    request_data['trialConcurrency'] = experiment_config['trialConcurrency']
    request_data['maxExecDuration'] = experiment_config['maxExecDuration']
    request_data['maxTrialNum'] = experiment_config['maxTrialNum']
    request_data['searchSpace'] = experiment_config.get('searchSpace')
    request_data['trainingServicePlatform'] = experiment_config.get('trainingServicePlatform')

    if experiment_config.get('description'):
        request_data['description'] = experiment_config['description']
    if experiment_config.get('multiPhase'):
        request_data['multiPhase'] = experiment_config.get('multiPhase')
    if experiment_config.get('multiThread'):
        request_data['multiThread'] = experiment_config.get('multiThread')
    if experiment_config.get('advisor'):
        request_data['advisor'] = experiment_config['advisor']
    else:
        request_data['tuner'] = experiment_config['tuner']
        if 'assessor' in experiment_config:
            request_data['assessor'] = experiment_config['assessor']
    #debug mode should disable version check
    if experiment_config.get('debug') is not None:
        request_data['versionCheck'] = not experiment_config.get('debug')
    if experiment_config.get('logCollection'):
        request_data['logCollection'] = experiment_config.get('logCollection')

    request_data['clusterMetaData'] = []
    if experiment_config['trainingServicePlatform'] == 'local':
        request_data['clusterMetaData'].append(
            {'key':'codeDir', 'value':experiment_config['trial']['codeDir']})
        request_data['clusterMetaData'].append(
            {'key': 'command', 'value': experiment_config['trial']['command']})
    elif experiment_config['trainingServicePlatform'] == 'remote':
        request_data['clusterMetaData'].append(
            {'key': 'machine_list', 'value': experiment_config['machineList']})
        request_data['clusterMetaData'].append(
            {'key': 'trial_config', 'value': experiment_config['trial']})
    elif experiment_config['trainingServicePlatform'] == 'pai':
        request_data['clusterMetaData'].append(
            {'key': 'pai_config', 'value': experiment_config['paiConfig']})        
        request_data['clusterMetaData'].append(
            {'key': 'trial_config', 'value': experiment_config['trial']})
    elif experiment_config['trainingServicePlatform'] == 'kubeflow':
        request_data['clusterMetaData'].append(
            {'key': 'kubeflow_config', 'value': experiment_config['kubeflowConfig']})
        request_data['clusterMetaData'].append(
            {'key': 'trial_config', 'value': experiment_config['trial']})
    elif experiment_config['trainingServicePlatform'] == 'frameworkcontroller':
        request_data['clusterMetaData'].append(
            {'key': 'frameworkcontroller_config', 'value': experiment_config['frameworkcontrollerConfig']})
        request_data['clusterMetaData'].append(
            {'key': 'trial_config', 'value': experiment_config['trial']})

    response = rest_post(experiment_url(port), json.dumps(request_data), REST_TIME_OUT, show_error=True)
    if check_response(response):
        return response
    else:
        _, stderr_full_path = get_log_path(config_file_name)
        if response is not None:
            with open(stderr_full_path, 'a+') as fout:
                fout.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True, separators=(',', ':')))
            print_error('Setting experiment error, error message is {}'.format(response.text))
        return None