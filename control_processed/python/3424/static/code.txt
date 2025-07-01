def resume_training(self, sgd=None, **cfg):
        """Continue training a pre-trained model.

        Create and return an optimizer, and initialize "rehearsal" for any pipeline
        component that has a .rehearse() method. Rehearsal is used to prevent
        models from "forgetting" their initialised "knowledge". To perform
        rehearsal, collect samples of text you want the models to retain performance
        on, and call nlp.rehearse() with a batch of Doc objects.
        """
        if cfg.get("device", -1) >= 0:
            util.use_gpu(cfg["device"])
            if self.vocab.vectors.data.shape[1] >= 1:
                self.vocab.vectors.data = Model.ops.asarray(self.vocab.vectors.data)
        link_vectors_to_models(self.vocab)
        if self.vocab.vectors.data.shape[1]:
            cfg["pretrained_vectors"] = self.vocab.vectors.name
        if sgd is None:
            sgd = create_default_optimizer(Model.ops)
        self._optimizer = sgd
        for name, proc in self.pipeline:
            if hasattr(proc, "_rehearsal_model"):
                proc._rehearsal_model = deepcopy(proc.model)
        return self._optimizer