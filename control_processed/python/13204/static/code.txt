def backbone_scope(freeze):
    """
    Args:
        freeze (bool): whether to freeze all the variables under the scope
    """
    def nonlin(x):
        x = get_norm()(x)
        return tf.nn.relu(x)

    with argscope([Conv2D, MaxPooling, BatchNorm], data_format='channels_first'), \
            argscope(Conv2D, use_bias=False, activation=nonlin,
                     kernel_initializer=tf.variance_scaling_initializer(
                         scale=2.0, mode='fan_out')), \
            ExitStack() as stack:
        if cfg.BACKBONE.NORM in ['FreezeBN', 'SyncBN']:
            if freeze or cfg.BACKBONE.NORM == 'FreezeBN':
                stack.enter_context(argscope(BatchNorm, training=False))
            else:
                stack.enter_context(argscope(
                    BatchNorm, sync_statistics='nccl' if cfg.TRAINER == 'replicated' else 'horovod'))

        if freeze:
            stack.enter_context(freeze_variables(stop_gradient=False, skip_collection=True))
        else:
            # the layers are not completely freezed, but we may want to only freeze the affine
            if cfg.BACKBONE.FREEZE_AFFINE:
                stack.enter_context(custom_getter_scope(freeze_affine_getter))
        yield