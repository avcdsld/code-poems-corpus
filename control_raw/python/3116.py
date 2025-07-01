def data(self)->Tensor:
        "Return the points associated to this object."
        flow = self.flow #This updates flow before we test if some transforms happened
        if self.transformed:
            if 'remove_out' not in self.sample_kwargs or self.sample_kwargs['remove_out']:
                flow = _remove_points_out(flow)
            self.transformed=False
        return flow.flow.flip(1)