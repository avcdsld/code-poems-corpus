def _init_params(self, inputs, overwrite=False):
        """Initialize weight parameters and auxiliary states."""
        inputs = [x if isinstance(x, DataDesc) else DataDesc(*x) for x in inputs]
        input_shapes = {item.name: item.shape for item in inputs}
        arg_shapes, _, aux_shapes = self.symbol.infer_shape(**input_shapes)
        assert arg_shapes is not None
        input_dtypes = {item.name: item.dtype for item in inputs}
        arg_dtypes, _, aux_dtypes = self.symbol.infer_type(**input_dtypes)
        assert arg_dtypes is not None

        arg_names = self.symbol.list_arguments()
        input_names = input_shapes.keys()
        param_names = [key for key in arg_names if key not in input_names]
        aux_names = self.symbol.list_auxiliary_states()

        param_name_attrs = [x for x in zip(arg_names, arg_shapes, arg_dtypes)
                            if x[0] in param_names]
        arg_params = {k : nd.zeros(shape=s, dtype=t)
                      for k, s, t in param_name_attrs}
        aux_name_attrs = [x for x in zip(aux_names, aux_shapes, aux_dtypes)
                          if x[0] in aux_names]
        aux_params = {k : nd.zeros(shape=s, dtype=t)
                      for k, s, t in aux_name_attrs}

        for k, v in arg_params.items():
            if self.arg_params and k in self.arg_params and (not overwrite):
                arg_params[k][:] = self.arg_params[k][:]
            else:
                self.initializer(k, v)

        for k, v in aux_params.items():
            if self.aux_params and k in self.aux_params and (not overwrite):
                aux_params[k][:] = self.aux_params[k][:]
            else:
                self.initializer(k, v)

        self.arg_params = arg_params
        self.aux_params = aux_params
        return (arg_names, list(param_names), aux_names)