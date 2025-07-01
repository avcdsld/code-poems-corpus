def log_uniform(low, high, size:Optional[List[int]]=None)->FloatOrTensor:
    "Draw 1 or shape=`size` random floats from uniform dist: min=log(`low`), max=log(`high`)."
    res = uniform(log(low), log(high), size)
    return exp(res) if size is None else res.exp_()