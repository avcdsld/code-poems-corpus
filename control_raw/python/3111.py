def clone(self):
        "Mimic the behavior of torch.clone for `ImagePoints` objects."
        return self.__class__(FlowField(self.size, self.flow.flow.clone()), scale=False, y_first=False)