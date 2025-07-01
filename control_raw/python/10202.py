def fetch_node_from(self, path):
        """ Returns a node for a path.

        :param path: Tuple of :term:`hashable` s.
        :rtype: :class:`~cerberus.errors.ErrorTreeNode` or :obj:`None`
        """
        context = self
        for key in path:
            context = context[key]
            if context is None:
                break
        return context