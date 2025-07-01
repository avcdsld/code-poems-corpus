def collect(self, name, arr):
        """Callback function for collecting layer output NDArrays."""
        name = py_str(name)
        if self.include_layer is not None and not self.include_layer(name):
            return
        handle = ctypes.cast(arr, NDArrayHandle)
        arr = NDArray(handle, writable=False).copyto(cpu())
        if self.logger is not None:
            self.logger.info("Collecting layer %s output of shape %s" % (name, arr.shape))
        if name in self.nd_dict:
            self.nd_dict[name].append(arr)
        else:
            self.nd_dict[name] = [arr]