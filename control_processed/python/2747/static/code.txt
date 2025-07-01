def fix_batchnorm(swa_model, train_dl):
    """
    During training, batch norm layers keep track of a running mean and
    variance of the previous layer's activations. Because the parameters
    of the SWA model are computed as the average of other models' parameters,
    the SWA model never sees the training data itself, and therefore has no
    opportunity to compute the correct batch norm statistics. Before performing 
    inference with the SWA model, we perform a single pass over the training data
    to calculate an accurate running mean and variance for each batch norm layer.
    """
    bn_modules = []
    swa_model.apply(lambda module: collect_bn_modules(module, bn_modules))
    
    if not bn_modules: return

    swa_model.train()

    for module in bn_modules:
        module.running_mean = torch.zeros_like(module.running_mean)
        module.running_var = torch.ones_like(module.running_var)
    
    momenta = [m.momentum for m in bn_modules]

    inputs_seen = 0

    for (*x,y) in iter(train_dl):        
        xs = V(x)
        batch_size = xs[0].size(0)

        momentum = batch_size / (inputs_seen + batch_size)
        for module in bn_modules:
            module.momentum = momentum
                            
        res = swa_model(*xs)        
        
        inputs_seen += batch_size
                
    for module, momentum in zip(bn_modules, momenta):
        module.momentum = momentum