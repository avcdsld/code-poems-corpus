def _get(self, field):
        """
        Return the value of a given field. The list of all queryable fields is
        detailed below, and can be obtained with the
        :func:`~turicreate.nearest_neighbors.NearestNeighborsModel._list_fields`
        method.

        +-----------------------+----------------------------------------------+
        |      Field            | Description                                  |
        +=======================+==============================================+
        | distance              | Measure of dissimilarity between two points  |
        +-----------------------+----------------------------------------------+
        | features              | Feature column names                         |
        +-----------------------+----------------------------------------------+
        | unpacked_features     | Names of the individual features used        |
        +-----------------------+----------------------------------------------+
        | label                 | Label column names                           |
        +-----------------------+----------------------------------------------+
        | leaf_size             | Max size of leaf nodes (ball tree only)      |
        +-----------------------+----------------------------------------------+
        | method                | Method of organizing reference data          |
        +-----------------------+----------------------------------------------+
        | num_examples          | Number of reference data observations        |
        +-----------------------+----------------------------------------------+
        | num_features          | Number of features for distance computation  |
        +-----------------------+----------------------------------------------+
        | num_unpacked_features | Number of unpacked features                  |
        +-----------------------+----------------------------------------------+
        | num_variables         | Number of variables for distance computation |
        +-----------------------+----------------------------------------------+
        | training_time         | Time to create the reference structure       |
        +-----------------------+----------------------------------------------+
        | tree_depth            | Number of levels in the tree (ball tree only)|
        +-----------------------+----------------------------------------------+

        Parameters
        ----------
        field : string
            Name of the field to be retrieved.

        Returns
        -------
        out
            Value of the requested field.
        """
        opts = {'model': self.__proxy__,
                'model_name': self.__name__,
                'field': field}
        response = _turicreate.extensions._nearest_neighbors.get_value(opts)
        return response['value']