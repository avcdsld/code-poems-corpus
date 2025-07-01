def utilization(self):
        """Percent of time over the past second was utilized.

        Details:
           Percent of time over the past second during which one or more kernels was executing on the GPU.
           Percent of time over the past second during which global (device) memory was being read or written

        Example:

            >>> print(ctx.device(0).utilization())
            {'gpu': 4L, 'memory': 6L}

        """
        class GpuUtilizationInfo(Structure):

            _fields_ = [
                ('gpu', c_uint),
                ('memory', c_uint),
            ]

        c_util = GpuUtilizationInfo()
        _check_return(_NVML.get_function(
            "nvmlDeviceGetUtilizationRates")(self.hnd, byref(c_util)))
        return {'gpu': c_util.gpu, 'memory': c_util.memory}