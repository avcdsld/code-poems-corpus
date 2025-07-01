def basic_critic(in_size:int, n_channels:int, n_features:int=64, n_extra_layers:int=0, **conv_kwargs):
    "A basic critic for images `n_channels` x `in_size` x `in_size`."
    layers = [conv_layer(n_channels, n_features, 4, 2, 1, leaky=0.2, norm_type=None, **conv_kwargs)]#norm_type=None?
    cur_size, cur_ftrs = in_size//2, n_features
    layers.append(nn.Sequential(*[conv_layer(cur_ftrs, cur_ftrs, 3, 1, leaky=0.2, **conv_kwargs) for _ in range(n_extra_layers)]))
    while cur_size > 4:
        layers.append(conv_layer(cur_ftrs, cur_ftrs*2, 4, 2, 1, leaky=0.2, **conv_kwargs))
        cur_ftrs *= 2 ; cur_size //= 2
    layers += [conv2d(cur_ftrs, 1, 4, padding=0), AvgFlatten()]
    return nn.Sequential(*layers)