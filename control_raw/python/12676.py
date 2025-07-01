def get_pre_compute(self, s):
        '''
        :param s: [src_sequence, batch_size, src_dim]
        :return: [src_sequence, batch_size. hidden_dim]
        '''
        hidden_dim = self.hidden_dim
        src_dim = s.get_shape().as_list()[-1]
        assert src_dim is not None, 'src dim must be defined'
        W = self._get_var('W', shape=[src_dim, hidden_dim])
        b = self._get_var('b', shape=[1, hidden_dim])
        return tf.tensordot(s, W, [[2], [0]]) + b