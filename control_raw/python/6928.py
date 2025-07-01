def train_batch(self, dataloader):
        """
        Description : training for LipNet
        """
        sum_losses = 0
        len_losses = 0
        for input_data, input_label in tqdm(dataloader):
            data = gluon.utils.split_and_load(input_data, self.ctx, even_split=False)
            label = gluon.utils.split_and_load(input_label, self.ctx, even_split=False)
            batch_size = input_data.shape[0]
            sum_losses, len_losses = self.train(data, label, batch_size)
            sum_losses += sum_losses
            len_losses += len_losses

        return sum_losses, len_losses