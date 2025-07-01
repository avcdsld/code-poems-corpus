def train_episode(agent, envs, preprocessors, t_max, render):
    """Complete an episode's worth of training for each environment."""
    num_envs = len(envs)

    # Buffers to hold trajectories, e.g. `env_xs[i]` will hold the observations
    # for environment `i`.
    env_xs, env_as = _2d_list(num_envs), _2d_list(num_envs)
    env_rs, env_vs = _2d_list(num_envs), _2d_list(num_envs)
    episode_rs = np.zeros(num_envs, dtype=np.float)

    for p in preprocessors:
        p.reset()

    observations = [p.preprocess(e.reset())
                    for p, e in zip(preprocessors, envs)]

    done = np.array([False for _ in range(num_envs)])
    all_done = False
    t = 1

    while not all_done:
        if render:
            envs[0].render()

        # NOTE(reed): Reshape to set the data shape.
        agent.model.reshape([('data', (num_envs, preprocessors[0].obs_size))])
        step_xs = np.vstack([o.ravel() for o in observations])

        # Get actions and values for all environments in a single forward pass.
        step_xs_nd = mx.nd.array(step_xs, ctx=agent.ctx)
        data_batch = mx.io.DataBatch(data=[step_xs_nd], label=None)
        agent.model.forward(data_batch, is_train=False)
        _, step_vs, _, step_ps = agent.model.get_outputs()

        step_ps = step_ps.asnumpy()
        step_vs = step_vs.asnumpy()
        step_as = agent.act(step_ps)

        # Step each environment whose episode has not completed.
        for i, env in enumerate(envs):
            if not done[i]:
                obs, r, done[i], _ = env.step(step_as[i])

                # Record the observation, action, value, and reward in the
                # buffers.
                env_xs[i].append(step_xs[i].ravel())
                env_as[i].append(step_as[i])
                env_vs[i].append(step_vs[i][0])
                env_rs[i].append(r)
                episode_rs[i] += r

                # Add 0 as the state value when done.
                if done[i]:
                    env_vs[i].append(0.0)
                else:
                    observations[i] = preprocessors[i].preprocess(obs)

        # Perform an update every `t_max` steps.
        if t == t_max:
            # If the episode has not finished, add current state's value. This
            # will be used to 'bootstrap' the final return (see Algorithm S3
            # in A3C paper).
            step_xs = np.vstack([o.ravel() for o in observations])
            step_xs_nd = mx.nd.array(step_xs, ctx=agent.ctx)
            data_batch = mx.io.DataBatch(data=[step_xs_nd], label=None)
            agent.model.forward(data_batch, is_train=False)
            _, extra_vs, _, _ = agent.model.get_outputs()
            extra_vs = extra_vs.asnumpy()
            for i in range(num_envs):
                if not done[i]:
                    env_vs[i].append(extra_vs[i][0])

            # Perform update and clear buffers.
            env_xs = np.vstack(list(chain.from_iterable(env_xs)))
            agent.train_step(env_xs, env_as, env_rs, env_vs)
            env_xs, env_as = _2d_list(num_envs), _2d_list(num_envs)
            env_rs, env_vs = _2d_list(num_envs), _2d_list(num_envs)
            t = 0

        all_done = np.all(done)
        t += 1

    return episode_rs