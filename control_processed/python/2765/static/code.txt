def plot(self, n_skip=10, n_skip_end=5):
        '''
        Plots the loss function with respect to learning rate, in log scale. 
        '''
        plt.ylabel("validation loss")
        plt.xlabel("learning rate (log scale)")
        plt.plot(self.lrs[n_skip:-(n_skip_end+1)], self.losses[n_skip:-(n_skip_end+1)])
        plt.xscale('log')