def tensor(x:Any, *rest)->Tensor:
    "Like `torch.as_tensor`, but handle lists too, and can pass multiple vector elements directly."
    if len(rest): x = (x,)+rest
    # XXX: Pytorch bug in dataloader using num_workers>0; TODO: create repro and report
    if is_listy(x) and len(x)==0: return tensor(0)
    res = torch.tensor(x) if is_listy(x) else as_tensor(x)
    if res.dtype is torch.int32:
        warn('Tensor is int32: upgrading to int64; for better performance use int64 input')
        return res.long()
    return res