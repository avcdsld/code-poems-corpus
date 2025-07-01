def update(self, max_norm=None):
        """Updates parameters according to the installed optimizer and the gradients computed
        in the previous forward-backward batch. Gradients are clipped by their global norm
        if `max_norm` is set.

        Parameters
        ----------
        max_norm: float, optional
            If set, clip values of all gradients the ratio of the sum of their norms.
        """
        if max_norm is not None:
            self._clip_by_global_norm(max_norm)
        self._module.update()