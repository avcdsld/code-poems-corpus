def _bind_ith_exec(self, i, data_shapes, label_shapes, shared_group):
        """Internal utility function to bind the i-th executor.
        This function utilizes simple_bind python interface.
        """
        shared_exec = None if shared_group is None else shared_group.execs[i]
        context = self.contexts[i]
        shared_data_arrays = self.shared_data_arrays[i]

        input_shapes = dict(data_shapes)
        if label_shapes is not None:
            input_shapes.update(dict(label_shapes))

        input_types = {x.name: x.dtype for x in data_shapes}
        if label_shapes is not None:
            input_types.update({x.name: x.dtype for x in label_shapes})

        group2ctx = self.group2ctxs[i]

        executor = self.symbol.simple_bind(ctx=context, grad_req=self.grad_req,
                                           type_dict=input_types, shared_arg_names=self.param_names,
                                           shared_exec=shared_exec, group2ctx=group2ctx,
                                           shared_buffer=shared_data_arrays, **input_shapes)
        self._total_exec_bytes += int(executor.debug_str().split('\n')[-3].split()[1])
        return executor