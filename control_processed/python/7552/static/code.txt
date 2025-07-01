def foreach(body, data, init_states):
    """Run a for loop with user-defined computation over NDArrays on dimension 0.

    This operator simulates a for loop and body has the computation for an iteration
    of the for loop. It runs the computation in body on each slice from the input
    NDArrays.

    body takes two arguments as input and outputs a tuple of two elements,
    as illustrated below::

        out, states = body(data1, states)

    data1 can be either an NDArray or a list of NDArrays. If data is an NDArray,
    data1 is an NDArray. Otherwise, data1 is a list of NDArrays and has the same
    size as data. states is a list of NDArrays and have the same size as init_states.
    Similarly, out can be either an NDArray or a list of NDArrays, which are concatenated
    as the first output of foreach; states from the last execution of body
    are the second output of foreach.

    The computation done by this operator is equivalent to the pseudo code below
    when the input data is NDArray::

        states = init_states
        outs = []
        for i in data.shape[0]:
            s = data[i]
            out, states = body(s, states)
            outs.append(out)
        outs = stack(*outs)


    Parameters
    ----------
    body : a Python function.
        Define computation in an iteration.
    data: an NDArray or a list of NDArrays.
        The input data.
    init_states: an NDArray or nested lists of NDArrays.
        The initial values of the loop states.
    name: string.
        The name of the operator.

    Returns
    -------
    outputs: an NDArray or nested lists of NDArrays.
        The output data concatenated from the output of all iterations.
    states: an NDArray or nested lists of NDArrays.
        The loop states in the last iteration.

    Examples
    --------
    >>> step = lambda data, states: (data + states[0], [states[0] * 2])
    >>> data = mx.nd.random.uniform(shape=(2, 10))
    >>> states = [mx.nd.random.uniform(shape=(10))]
    >>> outs, states = mx.nd.contrib.foreach(step, data, states)
    """

    def check_input(inputs, in_type, msg):
        is_NDArray_or_list = True
        if isinstance(inputs, list):
            for i in inputs:
                if not isinstance(i, in_type):
                    is_NDArray_or_list = False
                    break
        else:
            is_NDArray_or_list = isinstance(inputs, in_type)
        assert is_NDArray_or_list, msg

    flatten, _ = _flatten(data, "foreach input")
    check_input(flatten, ndarray.NDArray,
                "data should be an NDArray or a nested list of NDArrays")
    flatten, _ = _flatten(init_states, "foreach states")
    check_input(flatten, ndarray.NDArray,
                "init_states should be an NDArray or a nested list of NDArrays")

    not_data_list = isinstance(data, ndarray.NDArray)
    num_iters = data.shape[0] if not_data_list else data[0].shape[0]
    states = init_states
    outputs = []
    for i in range(num_iters):
        if not_data_list:
            eles = data[i]
        else:
            eles = [d[i] for d in data]
        outs, states = body(eles, states)
        outs, out_fmt = _flatten(outs, "foreach output")
        outputs.append(outs)
    outputs = zip(*outputs)
    tmp_outputs = []
    for out in outputs:
        tmp_outputs.append(ndarray.op.stack(*out))
    outputs = tmp_outputs
    outputs, _ = _regroup(outputs, out_fmt)

    return (outputs, states)