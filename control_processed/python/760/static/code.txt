def forward(self, input_ids, mems=None):
        """ Params:
                input_ids :: [bsz, len]
                mems :: optional mems from previous forwar passes (or init_mems)
                    list (num layers) of mem states at the entry of each layer
                        shape :: [self.config.mem_len, bsz, self.config.d_model]
                    Note that the first two dimensions are transposed in `mems` with regards to `input_ids` and `target`
            Returns:
                tuple (last_hidden, new_mems) where:
                    new_mems: list (num layers) of mem states at the entry of each layer
                        shape :: [self.config.mem_len, bsz, self.config.d_model]
                    last_hidden: output of the last layer:
                        shape :: [bsz, len, self.config.d_model]
        """
        # the original code for Transformer-XL used shapes [len, bsz] but we want a unified interface in the library
        # so we transpose here from shape [bsz, len] to shape [len, bsz]
        input_ids = input_ids.transpose(0, 1).contiguous()

        if mems is None:
            mems = self.init_mems(input_ids)
        last_hidden, new_mems = self._forward(input_ids, mems=mems)

        # We transpose back here to shape [bsz, len, hidden_dim]
        last_hidden = last_hidden.transpose(0, 1).contiguous()
        return (last_hidden, new_mems)