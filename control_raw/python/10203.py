def _insert_error(self, path, node):
        """ Adds an error or sub-tree to :attr:tree.

        :param path: Path to the error.
        :type path: Tuple of strings and integers.
        :param node: An error message or a sub-tree.
        :type node: String or dictionary.
        """
        field = path[0]
        if len(path) == 1:
            if field in self.tree:
                subtree = self.tree[field].pop()
                self.tree[field] += [node, subtree]
            else:
                self.tree[field] = [node, {}]
        elif len(path) >= 1:
            if field not in self.tree:
                self.tree[field] = [{}]
            subtree = self.tree[field][-1]

            if subtree:
                new = self.__class__(tree=copy(subtree))
            else:
                new = self.__class__()
            new._insert_error(path[1:], node)
            subtree.update(new.tree)