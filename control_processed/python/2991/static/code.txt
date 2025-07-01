def explained_variance(pred:Tensor, targ:Tensor)->Rank0Tensor:
    "Explained variance between `pred` and `targ`."
    pred,targ = flatten_check(pred,targ)
    var_pct = torch.var(targ - pred) / torch.var(targ)
    return 1 - var_pct