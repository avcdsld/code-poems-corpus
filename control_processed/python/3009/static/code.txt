def _jitter(c, magnitude:uniform):
    "Replace pixels by random neighbors at `magnitude`."
    c.flow.add_((torch.rand_like(c.flow)-0.5)*magnitude*2)
    return c