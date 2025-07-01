def get_model(self, opt_fn, emb_sz, n_hid, n_layers, **kwargs):
        """ Method returns a RNN_Learner object, that wraps an instance of the RNN_Encoder module.

        Args:
            opt_fn (Optimizer): the torch optimizer function to use
            emb_sz (int): embedding size
            n_hid (int): number of hidden inputs
            n_layers (int): number of hidden layers
            kwargs: other arguments

        Returns:
            An instance of the RNN_Learner class.

        """
        m = get_language_model(self.nt, emb_sz, n_hid, n_layers, self.pad_idx, **kwargs)
        model = SingleModel(to_gpu(m))
        return RNN_Learner(self, model, opt_fn=opt_fn)