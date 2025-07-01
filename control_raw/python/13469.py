def allreduce_grads_hierarchical(all_grads, devices, average=False):
    """
    Hierarchical allreduce for DGX-1 system.

    Args:
        all_grads (K x N): List of list of gradients. N is the number of variables.
        devices ([str]): K str for the K devices.
        average (bool): average gradients or not.

    Returns:
        (K x N): same as input, but each grad is replaced by the average over K lists.
    """
    num_gpu = len(devices)
    assert num_gpu == 8, num_gpu
    assert len(all_grads) == num_gpu, len(all_grads)
    group_size = num_gpu // 2

    agg_all_grads = []  # N x K
    for varid, grads in enumerate(zip(*all_grads)):
        # grads: K gradients
        g0_main_gpu = varid % num_gpu
        g1_main_gpu = (g0_main_gpu + group_size) % num_gpu
        g0_start = 0 if g0_main_gpu < group_size else group_size
        g1_start = 0 if g1_main_gpu < group_size else group_size
        assert g0_start != g1_start
        g0_grads = grads[g0_start: g0_start + group_size]
        g1_grads = grads[g1_start: g1_start + group_size]

        with tf.device(devices[g0_main_gpu]):
            g0_agg = tf.add_n(g0_grads, name='group0_agg')

        with tf.device(devices[g1_main_gpu]):
            g1_agg = tf.add_n(g1_grads, name='group1_agg')
            g1_total_agg = tf.add(g0_agg, g1_agg, name='group1_total_agg')

        with tf.device(devices[g0_main_gpu]):
            g0_total_agg = tf.identity(g1_total_agg, name='group0_total_agg')

        agg_grads = []  # K aggregated grads
        for k in range(num_gpu):
            if (k < group_size) == (g0_main_gpu < group_size):
                main_gpu = g0_total_agg
            else:
                main_gpu = g1_total_agg
            with tf.device(devices[k]):
                if not average:
                    device_total_agg = tf.identity(
                        main_gpu, name='device{}_total_agg'.format(k))
                else:
                    # TODO where to put average?
                    device_total_agg = tf.multiply(
                        main_gpu, 1.0 / num_gpu, name='device{}_total_agg'.format(k))
                agg_grads.append(device_total_agg)

        agg_all_grads.append(agg_grads)

    # transpose
    agg_all_grads = list(zip(*agg_all_grads))   # K x Nvar
    return agg_all_grads