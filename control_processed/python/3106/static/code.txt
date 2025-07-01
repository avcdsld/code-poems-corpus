def resize(self, size:Union[int,TensorImageSize])->'Image':
        "Resize the image to `size`, size can be a single int."
        assert self._flow is None
        if isinstance(size, int): size=(self.shape[0], size, size)
        if tuple(size)==tuple(self.shape): return self
        self.flow = _affine_grid(size)
        return self