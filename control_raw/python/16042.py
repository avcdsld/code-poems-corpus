def add_leaf_node(self, tree_id, node_id, values, relative_hit_rate = None):
        """
        Add a leaf node to the tree ensemble.

        Parameters
        ----------
        tree_id: int
            ID of the tree to add the node to.

        node_id: int
            ID of the node within the tree.

        values: [float | int | list | dict]
            Value(s) at the leaf node to add to the prediction when this node is
            activated.  If the prediction dimension of the tree is 1, then the
            value is specified as a float or integer value.

            For multidimensional predictions, the values can be a list of numbers
            with length matching the dimension of the predictions or a dictionary
            mapping index to value added to that dimension.

            Note that the dimension of any tree must match the dimension given
            when :py:meth:`set_default_prediction_value` is called.

        """
        spec_node = self.tree_parameters.nodes.add()
        spec_node.treeId = tree_id
        spec_node.nodeId = node_id
        spec_node.nodeBehavior = \
           _TreeEnsemble_pb2.TreeEnsembleParameters.TreeNode.TreeNodeBehavior.Value('LeafNode')

        if not isinstance(values, _collections.Iterable):
            values = [values]

        if relative_hit_rate is not None:
            spec_node.relativeHitRate = relative_hit_rate

        if type(values) == dict:
            iter = values.items()
        else:
            iter = enumerate(values)

        for index, value in iter:
            ev_info = spec_node.evaluationInfo.add()
            ev_info.evaluationIndex = index
            ev_info.evaluationValue = float(value)
            spec_node.nodeBehavior = \
                _TreeEnsemble_pb2.TreeEnsembleParameters.TreeNode.TreeNodeBehavior.Value('LeafNode')