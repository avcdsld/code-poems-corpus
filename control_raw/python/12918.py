def legal_graph(graph):
    '''judge if a graph is legal or not.
    '''

    descriptor = graph.extract_descriptor()
    skips = descriptor.skip_connections
    if len(skips) != len(set(skips)):
        return False
    return True