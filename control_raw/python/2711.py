def on_batch_end(self, last_loss:Tensor, iteration:int, **kwargs)->None:
        "Callback function that writes batch end appropriate data to Tensorboard."
        if iteration == 0: return
        self._update_batches_if_needed()
        if iteration % self.loss_iters == 0: self._write_training_loss(iteration=iteration, last_loss=last_loss)
        if iteration % self.hist_iters == 0: self._write_weight_histograms(iteration=iteration)