def to_graphviz(booster, fmap='', num_trees=0, rankdir='UT',
                yes_color='#0000FF', no_color='#FF0000',
                condition_node_params=None, leaf_node_params=None, **kwargs):
    """Convert specified tree to graphviz instance. IPython can automatically plot the
    returned graphiz instance. Otherwise, you should call .render() method
    of the returned graphiz instance.

    Parameters
    ----------
    booster : Booster, XGBModel
        Booster or XGBModel instance
    fmap: str (optional)
       The name of feature map file
    num_trees : int, default 0
        Specify the ordinal number of target tree
    rankdir : str, default "UT"
        Passed to graphiz via graph_attr
    yes_color : str, default '#0000FF'
        Edge color when meets the node condition.
    no_color : str, default '#FF0000'
        Edge color when doesn't meet the node condition.
    condition_node_params : dict (optional)
        condition node configuration,
        {'shape':'box',
               'style':'filled,rounded',
               'fillcolor':'#78bceb'
        }
    leaf_node_params : dict (optional)
        leaf node configuration
        {'shape':'box',
               'style':'filled',
               'fillcolor':'#e48038'
        }
    kwargs :
        Other keywords passed to graphviz graph_attr

    Returns
    -------
    ax : matplotlib Axes
    """

    if condition_node_params is None:
        condition_node_params = {}
    if leaf_node_params is None:
        leaf_node_params = {}

    try:
        from graphviz import Digraph
    except ImportError:
        raise ImportError('You must install graphviz to plot tree')

    if not isinstance(booster, (Booster, XGBModel)):
        raise ValueError('booster must be Booster or XGBModel instance')

    if isinstance(booster, XGBModel):
        booster = booster.get_booster()

    tree = booster.get_dump(fmap=fmap)[num_trees]
    tree = tree.split()

    kwargs = kwargs.copy()
    kwargs.update({'rankdir': rankdir})
    graph = Digraph(graph_attr=kwargs)

    for i, text in enumerate(tree):
        if text[0].isdigit():
            node = _parse_node(
                graph, text, condition_node_params=condition_node_params,
                leaf_node_params=leaf_node_params)
        else:
            if i == 0:
                # 1st string must be node
                raise ValueError('Unable to parse given string as tree')
            _parse_edge(graph, node, text, yes_color=yes_color,
                        no_color=no_color)

    return graph