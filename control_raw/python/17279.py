def train(self, input, label):
        """
        Submits an input batch to the model. Returns a MpsFloatArray
        representing the batch loss. Calling asnumpy() on this value will wait
        for the batch to finish and yield the loss as a numpy array.
        """

        assert self._mode == MpsGraphMode.Train
        assert input.shape == self._ishape
        assert label.shape == self._oshape

        input_array = MpsFloatArray(input)
        label_array = MpsFloatArray(label)
        result_handle = _ctypes.c_void_p()
        status_code = self._LIB.TCMPSTrainGraph(
            self.handle, input_array.handle, label_array.handle,
            _ctypes.byref(result_handle))

        assert status_code == 0, "Error calling TCMPSTrainGraph"
        assert result_handle, "TCMPSTrainGraph unexpectedly returned NULL pointer"

        result = MpsFloatArray(result_handle)

        # Output from training should be a one-dimensional array of loss values,
        # one per example in the batch.
        assert result.shape() == (self._oshape[0],)

        return result