def gpu_mem_get(id=None):
    "get total, used and free memory (in MBs) for gpu `id`. if `id` is not passed, currently selected torch device is used"
    if not use_gpu: return GPUMemory(0, 0, 0)
    if id is None: id = torch.cuda.current_device()
    try:
        handle = pynvml.nvmlDeviceGetHandleByIndex(id)
        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        return GPUMemory(*(map(b2mb, [info.total, info.free, info.used])))
    except:
        return GPUMemory(0, 0, 0)