def pack_all(self, all_grads, devices):
        """
        Args:
            all_grads: K x N, K lists of gradients to be packed
        """
        ret = []    # #GPU x #split
        for dev, grads in zip(devices, all_grads):
            with tf.device(dev):
                ret.append(self.pack(grads))
        return ret