def predict_topk(self, dataset, output_type="probability", k=3, batch_size=64):
        """
        Return top-k predictions for the ``dataset``, using the trained model.
        Predictions are returned as an SFrame with three columns: `id`,
        `class`, and `probability`, `margin`,  or `rank`, depending on the ``output_type``
        parameter. Input dataset size must be the same as for training of the model.

        Parameters
        ----------
        dataset : SFrame | SArray | turicreate.Image
            Images to be classified.
            If dataset is an SFrame, it must include columns with the same
            names as the features used for model training, but does not require
            a target column. Additional columns are ignored.

        output_type : {'probability', 'rank', 'margin'}, optional
            Choose the return type of the prediction:

            - `probability`: Probability associated with each label in the prediction.
            - `rank`       : Rank associated with each label in the prediction.
            - `margin`     : Margin associated with each label in the prediction.

        k : int, optional
            Number of classes to return for each input example.

        Returns
        -------
        out : SFrame
            An SFrame with model predictions.

        See Also
        --------
        predict, classify, evaluate

        Examples
        --------
        >>> pred = m.predict_topk(validation_data, k=3)
        >>> pred
        +----+-------+-------------------+
        | id | class |   probability     |
        +----+-------+-------------------+
        | 0  |   4   |   0.995623886585  |
        | 0  |   9   |  0.0038311756216  |
        | 0  |   7   | 0.000301006948575 |
        | 1  |   1   |   0.928708016872  |
        | 1  |   3   |  0.0440889261663  |
        | 1  |   2   |  0.0176190119237  |
        | 2  |   3   |   0.996967732906  |
        | 2  |   2   |  0.00151345680933 |
        | 2  |   7   | 0.000637513934635 |
        | 3  |   1   |   0.998070061207  |
        | .. |  ...  |        ...        |
        +----+-------+-------------------+
        [35688 rows x 3 columns]
        """
        if not isinstance(dataset, (_tc.SFrame, _tc.SArray, _tc.Image)):
            raise TypeError('dataset must be either an SFrame, SArray or turicreate.Image')
        if(batch_size < 1):
            raise ValueError("'batch_size' must be greater than or equal to 1")

        dataset, _ = self._canonize_input(dataset)

        extracted_features = self._extract_features(dataset)
        return self.classifier.predict_topk(extracted_features, output_type = output_type, k = k)