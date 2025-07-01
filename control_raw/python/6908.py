def check_label_shape(self, label_shape):
        """Checks if the new label shape is valid"""
        if not len(label_shape) == 2:
            raise ValueError('label_shape should have length 2')
        if label_shape[0] < self.label_shape[0]:
            msg = 'Attempts to reduce label count from %d to %d, not allowed.' \
                % (self.label_shape[0], label_shape[0])
            raise ValueError(msg)
        if label_shape[1] != self.provide_label[0][1][2]:
            msg = 'label_shape object width inconsistent: %d vs %d.' \
                % (self.provide_label[0][1][2], label_shape[1])
            raise ValueError(msg)