def get_post_init_ops():
        """
        Copy values of variables on GPU 0 to other GPUs.
        """
        # literally all variables, because it's better to sync optimizer-internal variables as well
        all_vars = tf.global_variables() + tf.local_variables()
        var_by_name = dict([(v.name, v) for v in all_vars])
        trainable_names = set([x.name for x in tf.trainable_variables()])
        post_init_ops = []

        def log_failure(name, reason):
            logger.warn("[ReplicatedTrainer] Do not know how to sync variable '{}' across GPUs. "
                        "Reason: {} ".format(name, reason))
            assert name not in trainable_names, \
                "The aforementioned variable is trainable, so this is probably a fatal error."
            logger.warn(
                "[ReplicatedTrainer] This variable is non-trainable. "
                "Ignore this warning if you know it's OK to leave it out-of-sync.")

        for v in all_vars:
            if not v.name.startswith('tower'):
                continue
            if v.name.startswith('tower0'):
                # in this trainer, the master name doesn't have the towerx/ prefix
                log_failure(v.name, "Name should not have prefix 'tower0' in this trainer!")
                continue        # TODO some vars (EMA) may still startswith tower0

            split_name = v.name.split('/')
            prefix = split_name[0]
            realname = '/'.join(split_name[1:])
            if prefix in realname:
                log_failure(v.name, "Prefix {} appears multiple times in its name!".format(prefix))
                continue
            copy_from = var_by_name.get(realname)
            if copy_from is not None:
                post_init_ops.append(v.assign(copy_from.read_value()))
            else:
                log_failure(v.name, "Cannot find {} in the graph!".format(realname))
        logger.info(
            "'sync_variables_from_main_tower' includes {} operations.".format(len(post_init_ops)))
        return tf.group(*post_init_ops, name='sync_variables_from_main_tower')