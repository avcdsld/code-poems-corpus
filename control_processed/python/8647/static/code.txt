def _env_runner(base_env, extra_batch_callback, policies, policy_mapping_fn,
                unroll_length, horizon, preprocessors, obs_filters,
                clip_rewards, clip_actions, pack, callbacks, tf_sess,
                perf_stats, soft_horizon):
    """This implements the common experience collection logic.

    Args:
        base_env (BaseEnv): env implementing BaseEnv.
        extra_batch_callback (fn): function to send extra batch data to.
        policies (dict): Map of policy ids to PolicyGraph instances.
        policy_mapping_fn (func): Function that maps agent ids to policy ids.
            This is called when an agent first enters the environment. The
            agent is then "bound" to the returned policy for the episode.
        unroll_length (int): Number of episode steps before `SampleBatch` is
            yielded. Set to infinity to yield complete episodes.
        horizon (int): Horizon of the episode.
        preprocessors (dict): Map of policy id to preprocessor for the
            observations prior to filtering.
        obs_filters (dict): Map of policy id to filter used to process
            observations for the policy.
        clip_rewards (bool): Whether to clip rewards before postprocessing.
        pack (bool): Whether to pack multiple episodes into each batch. This
            guarantees batches will be exactly `unroll_length` in size.
        clip_actions (bool): Whether to clip actions to the space range.
        callbacks (dict): User callbacks to run on episode events.
        tf_sess (Session|None): Optional tensorflow session to use for batching
            TF policy evaluations.
        perf_stats (PerfStats): Record perf stats into this object.
        soft_horizon (bool): Calculate rewards but don't reset the
            environment when the horizon is hit.

    Yields:
        rollout (SampleBatch): Object containing state, action, reward,
            terminal condition, and other fields as dictated by `policy`.
    """

    try:
        if not horizon:
            horizon = (base_env.get_unwrapped()[0].spec.max_episode_steps)
    except Exception:
        logger.debug("no episode horizon specified, assuming inf")
    if not horizon:
        horizon = float("inf")

    # Pool of batch builders, which can be shared across episodes to pack
    # trajectory data.
    batch_builder_pool = []

    def get_batch_builder():
        if batch_builder_pool:
            return batch_builder_pool.pop()
        else:
            return MultiAgentSampleBatchBuilder(
                policies, clip_rewards, callbacks.get("on_postprocess_traj"))

    def new_episode():
        episode = MultiAgentEpisode(policies, policy_mapping_fn,
                                    get_batch_builder, extra_batch_callback)
        if callbacks.get("on_episode_start"):
            callbacks["on_episode_start"]({
                "env": base_env,
                "policy": policies,
                "episode": episode,
            })
        return episode

    active_episodes = defaultdict(new_episode)

    while True:
        perf_stats.iters += 1
        t0 = time.time()
        # Get observations from all ready agents
        unfiltered_obs, rewards, dones, infos, off_policy_actions = \
            base_env.poll()
        perf_stats.env_wait_time += time.time() - t0

        if log_once("env_returns"):
            logger.info("Raw obs from env: {}".format(
                summarize(unfiltered_obs)))
            logger.info("Info return from env: {}".format(summarize(infos)))

        # Process observations and prepare for policy evaluation
        t1 = time.time()
        active_envs, to_eval, outputs = _process_observations(
            base_env, policies, batch_builder_pool, active_episodes,
            unfiltered_obs, rewards, dones, infos, off_policy_actions, horizon,
            preprocessors, obs_filters, unroll_length, pack, callbacks,
            soft_horizon)
        perf_stats.processing_time += time.time() - t1
        for o in outputs:
            yield o

        # Do batched policy eval
        t2 = time.time()
        eval_results = _do_policy_eval(tf_sess, to_eval, policies,
                                       active_episodes)
        perf_stats.inference_time += time.time() - t2

        # Process results and update episode state
        t3 = time.time()
        actions_to_send = _process_policy_eval_results(
            to_eval, eval_results, active_episodes, active_envs,
            off_policy_actions, policies, clip_actions)
        perf_stats.processing_time += time.time() - t3

        # Return computed actions to ready envs. We also send to envs that have
        # taken off-policy actions; those envs are free to ignore the action.
        t4 = time.time()
        base_env.send_actions(actions_to_send)
        perf_stats.env_wait_time += time.time() - t4