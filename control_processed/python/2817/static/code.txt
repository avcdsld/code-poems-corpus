def most_by_uncertain(self, y):
        """ Extracts the predicted classes which correspond to the selected class (y) and have probabilities nearest to 1/number_of_classes (eg. 0.5 for 2 classes, 0.33 for 3 classes) for the selected class.

            Arguments:
                y (int): the selected class

            Returns:
                idxs (numpy.ndarray): An array of indexes (numpy.ndarray)
        """
        return self.most_uncertain_by_mask((self.ds.y == y), y)