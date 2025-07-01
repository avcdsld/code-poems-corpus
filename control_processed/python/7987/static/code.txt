def backward(self, out_grads=None, is_train=True):
        """Do backward pass to get the gradient of arguments.

        Parameters
        ----------
        out_grads : NDArray or list of NDArray or dict of str to NDArray, optional
            Gradient on the outputs to be propagated back.
            This parameter is only needed when bind is called
            on outputs that are not a loss function.
        is_train : bool, default True
            Whether this backward is for training or inference. Note that in rare
            cases you want to call backward with is_train=False to get gradient
            during inference.


        Examples
        --------
        >>> # Example for binding on loss function symbol, which gives the loss value of the model.
        >>> # Equivalently it gives the head gradient for backward pass.
        >>> # In this example the built-in SoftmaxOutput is used as loss function.
        >>> # MakeLoss can be used to define customized loss function symbol.
        >>> net = mx.sym.Variable('data')
        >>> net = mx.sym.FullyConnected(net, name='fc', num_hidden=6)
        >>> net = mx.sym.Activation(net, name='relu', act_type="relu")
        >>> net = mx.sym.SoftmaxOutput(net, name='softmax')

        >>> args =  {'data': mx.nd.ones((1, 4)), 'fc_weight': mx.nd.ones((6, 4)),
        >>>          'fc_bias': mx.nd.array((1, 4, 4, 4, 5, 6)), 'softmax_label': mx.nd.ones((1))}
        >>> args_grad = {'fc_weight': mx.nd.zeros((6, 4)), 'fc_bias': mx.nd.zeros((6))}
        >>> texec = net.bind(ctx=mx.cpu(), args=args, args_grad=args_grad)
        >>> out = texec.forward(is_train=True)[0].copy()
        >>> print out.asnumpy()
        [[ 0.00378404  0.07600445  0.07600445  0.07600445  0.20660152  0.5616011 ]]
        >>> texec.backward()
        >>> print(texec.grad_arrays[1].asnumpy())
        [[ 0.00378404  0.00378404  0.00378404  0.00378404]
         [-0.92399555 -0.92399555 -0.92399555 -0.92399555]
         [ 0.07600445  0.07600445  0.07600445  0.07600445]
         [ 0.07600445  0.07600445  0.07600445  0.07600445]
         [ 0.20660152  0.20660152  0.20660152  0.20660152]
         [ 0.5616011   0.5616011   0.5616011   0.5616011 ]]
        >>>
        >>> # Example for binding on non-loss function symbol.
        >>> # Here the binding symbol is neither built-in loss function
        >>> # nor customized loss created by MakeLoss.
        >>> # As a result the head gradient is not automatically provided.
        >>> a = mx.sym.Variable('a')
        >>> b = mx.sym.Variable('b')
        >>> # c is not a loss function symbol
        >>> c = 2 * a + b
        >>> args = {'a': mx.nd.array([1,2]), 'b':mx.nd.array([2,3])}
        >>> args_grad = {'a': mx.nd.zeros((2)), 'b': mx.nd.zeros((2))}
        >>> texec = c.bind(ctx=mx.cpu(), args=args, args_grad=args_grad)
        >>> out = texec.forward(is_train=True)[0].copy()
        >>> print(out.asnumpy())
        [ 4.  7.]
        >>> # out_grads is the head gradient in backward pass.
        >>> # Here we define 'c' as loss function.
        >>> # Then 'out' is passed as head gradient of backward pass.
        >>> texec.backward(out)
        >>> print(texec.grad_arrays[0].asnumpy())
        [ 8.  14.]
        >>> print(texec.grad_arrays[1].asnumpy())
        [ 4.  7.]
        """
        if out_grads is None:
            out_grads = []
        elif isinstance(out_grads, NDArray):
            out_grads = [out_grads]
        elif isinstance(out_grads, dict):
            out_grads = [out_grads[k] for k in self._symbol.list_outputs()]

        for obj in out_grads:
            if not isinstance(obj, NDArray):
                raise TypeError("inputs must be NDArray")
        ndarray = c_handle_array(out_grads)
        check_call(_LIB.MXExecutorBackwardEx(
            self.handle,
            mx_uint(len(out_grads)),
            ndarray,
            ctypes.c_int(is_train)))