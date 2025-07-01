def sorted_tree(tree):
    """Sorts the dict representation of the tree

    The root packages as well as the intermediate packages are sorted
    in the alphabetical order of the package names.

    :param dict tree: the pkg dependency tree obtained by calling
                     `construct_tree` function
    :returns: sorted tree
    :rtype: collections.OrderedDict

    """
    return OrderedDict(sorted([(k, sorted(v, key=attrgetter('key')))
                               for k, v in tree.items()],
                              key=lambda kv: kv[0].key))