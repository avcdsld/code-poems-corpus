def on_epoch_end(self, epoch, **kwargs:Any)->None:
        "Send loss and metrics values to MLFlow after each epoch"
        if kwargs['smooth_loss'] is None or kwargs["last_metrics"] is None: return
        metrics = [kwargs['smooth_loss']] + kwargs["last_metrics"]
        for name, val in zip(self.metrics_names, metrics):
            self.client.log_metric(self.run, name, np.float(val))