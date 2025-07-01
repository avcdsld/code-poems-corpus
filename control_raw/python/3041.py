def on_backward_begin(self, last_loss:Rank0Tensor, last_input:Tensor, **kwargs):
        "Apply AR and TAR to `last_loss`."
        #AR and TAR
        if self.alpha != 0.:  last_loss += self.alpha * self.out[-1].float().pow(2).mean()
        if self.beta != 0.:
            h = self.raw_out[-1]
            if len(h)>1: last_loss += self.beta * (h[:,1:] - h[:,:-1]).float().pow(2).mean()
        return {'last_loss': last_loss}