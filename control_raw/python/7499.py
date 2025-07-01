def save_params(self, fname):
        """Saves model parameters to file.

        Parameters
        ----------
        fname : str
            Path to output param file.

        Examples
        --------
        >>> # An example of saving module parameters.
        >>> mod.save_params('myfile')
        """
        arg_params, aux_params = self.get_params()
        save_dict = {('arg:%s' % k) : v.as_in_context(cpu()) for k, v in arg_params.items()}
        save_dict.update({('aux:%s' % k) : v.as_in_context(cpu()) for k, v in aux_params.items()})
        ndarray.save(fname, save_dict)