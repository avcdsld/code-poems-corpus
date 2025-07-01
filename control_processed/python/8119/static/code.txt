def run_experiments(experiments,
                    search_alg=None,
                    scheduler=None,
                    with_server=False,
                    server_port=TuneServer.DEFAULT_PORT,
                    verbose=2,
                    resume=False,
                    queue_trials=False,
                    reuse_actors=False,
                    trial_executor=None,
                    raise_on_failed_trial=True):
    """Runs and blocks until all trials finish.

    Examples:
        >>> experiment_spec = Experiment("experiment", my_func)
        >>> run_experiments(experiments=experiment_spec)

        >>> experiment_spec = {"experiment": {"run": my_func}}
        >>> run_experiments(experiments=experiment_spec)

        >>> run_experiments(
        >>>     experiments=experiment_spec,
        >>>     scheduler=MedianStoppingRule(...))

        >>> run_experiments(
        >>>     experiments=experiment_spec,
        >>>     search_alg=SearchAlgorithm(),
        >>>     scheduler=MedianStoppingRule(...))

    Returns:
        List of Trial objects, holding data for each executed trial.

    """
    # This is important to do this here
    # because it schematize the experiments
    # and it conducts the implicit registration.
    experiments = convert_to_experiment_list(experiments)

    trials = []
    for exp in experiments:
        trials += run(
            exp,
            search_alg=search_alg,
            scheduler=scheduler,
            with_server=with_server,
            server_port=server_port,
            verbose=verbose,
            resume=resume,
            queue_trials=queue_trials,
            reuse_actors=reuse_actors,
            trial_executor=trial_executor,
            raise_on_failed_trial=raise_on_failed_trial)
    return trials