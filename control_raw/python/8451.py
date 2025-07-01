def _autodetect_num_gpus():
    """Attempt to detect the number of GPUs on this machine.

    TODO(rkn): This currently assumes Nvidia GPUs and Linux.

    Returns:
        The number of GPUs if any were detected, otherwise 0.
    """
    proc_gpus_path = "/proc/driver/nvidia/gpus"
    if os.path.isdir(proc_gpus_path):
        return len(os.listdir(proc_gpus_path))
    return 0