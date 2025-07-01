def plot_by_correct(self, y, is_correct):
        """ Plots the images which correspond to the selected class (y) and to the specific case (prediction is correct - is_true=True, prediction is wrong - is_true=False)

            Arguments:
                y (int): the selected class
                is_correct (boolean): a boolean flag (True, False) which specify the what to look for. Ex: True - most correct samples, False - most incorrect samples
        """
        return self.plot_val_with_title(self.most_by_correct(y, is_correct), y)