def _get(self, field):
        """
        Return the value of a given field.

        +-----------------------+----------------------------------------------+
        |      Field            | Description                                  |
        +=======================+==============================================+
        | batch_size            | Number of randomly chosen examples to use in |
        |                       | each training iteration.                     |
        +-----------------------+----------------------------------------------+
        | cluster_id            | Cluster assignment for each data point and   |
        |                       | Euclidean distance to the cluster center     |
        +-----------------------+----------------------------------------------+
        | cluster_info          | Cluster centers, sum of squared Euclidean    |
        |                       | distances from each cluster member to the    |
        |                       | assigned center, and the number of data      |
        |                       | points belonging to the cluster              |
        +-----------------------+----------------------------------------------+
        | features              | Names of feature columns                     |
        +-----------------------+----------------------------------------------+
        | max_iterations        | Maximum number of iterations to perform      |
        +-----------------------+----------------------------------------------+
        | method                | Algorithm used to train the model.           |
        +-----------------------+----------------------------------------------+
        | num_clusters          | Number of clusters                           |
        +-----------------------+----------------------------------------------+
        | num_examples          | Number of examples in the dataset            |
        +-----------------------+----------------------------------------------+
        | num_features          | Number of feature columns used               |
        +-----------------------+----------------------------------------------+
        | num_unpacked_features | Number of features unpacked from the         |
        |                       | feature columns                              |
        +-----------------------+----------------------------------------------+
        | training_iterations   | Total number of iterations performed         |
        +-----------------------+----------------------------------------------+
        | training_time         | Total time taken to cluster the data         |
        +-----------------------+----------------------------------------------+
        | unpacked_features     | Names of features unpacked from the          |
        |                       | feature columns                              |
        +-----------------------+----------------------------------------------+

        Parameters
        ----------
        field : str
            The name of the field to query.

        Returns
        -------
        out
            Value of the requested field
        """
        opts = {'model': self.__proxy__,
                'model_name': self.__name__,
                'field': field}
        response = _tc.extensions._kmeans.get_value(opts)

        return response['value']