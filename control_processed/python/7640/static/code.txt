def update_metric(self, eval_metric, labels, pre_sliced=False):
        """Evaluates and accumulates evaluation metric on outputs of the last forward computation.

        See Also
        ----------
        :meth:`BaseModule.update_metric`.

        Parameters
        ----------
        eval_metric : EvalMetric
            Evaluation metric to use.
        labels : list of NDArray if `pre_sliced` parameter is set to `False`,
            list of lists of NDArray otherwise. Typically `data_batch.label`.
        pre_sliced: bool
            Whether the labels are already sliced per device (default: False).
        """
        self._exec_group.update_metric(eval_metric, labels, pre_sliced)