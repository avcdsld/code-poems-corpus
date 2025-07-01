def memory(self):
        """Memory information in bytes

        Example:

            >>> print(ctx.device(0).memory())
            {'total': 4238016512L, 'used': 434831360L, 'free': 3803185152L}

        Returns:
            total/used/free memory in bytes
        """
        class GpuMemoryInfo(Structure):
            _fields_ = [
                ('total', c_ulonglong),
                ('free', c_ulonglong),
                ('used', c_ulonglong),
            ]

        c_memory = GpuMemoryInfo()
        _check_return(_NVML.get_function(
            "nvmlDeviceGetMemoryInfo")(self.hnd, byref(c_memory)))
        return {'total': c_memory.total, 'free': c_memory.free, 'used': c_memory.used}