def one_cycle_scheduler(lr_max:float, **kwargs:Any)->OneCycleScheduler:
    "Instantiate a `OneCycleScheduler` with `lr_max`."
    return partial(OneCycleScheduler, lr_max=lr_max, **kwargs)