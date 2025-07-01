def get_params(self):
        """Gets current parameters.

        Returns
        -------
        (arg_params, aux_params)
            A pair of dictionaries each mapping parameter names to NDArray values. This
            is a merged dictionary of all the parameters in the modules.
        """
        assert self.binded and self.params_initialized

        arg_params = dict()
        aux_params = dict()

        for module in self._modules:
            arg, aux = module.get_params()
            arg_params.update(arg)
            aux_params.update(aux)

        return (arg_params, aux_params)