def differentiate_prefix(path_components0, path_components1):
    """
    Return the differentiated prefix of the given two iterables. 
     
    Taken from https://stackoverflow.com/q/21498939/438386
    """
    longest_prefix = []
    root_comparison = False
    common_elmt = None
    for index, (elmt0, elmt1) in enumerate(zip(path_components0, path_components1)):
        if elmt0 != elmt1:
            if index == 2:
                root_comparison = True
            break
        else:
            common_elmt = elmt0
        longest_prefix.append(elmt0)
    file_name_length = len(path_components0[len(path_components0) - 1])
    path_0 = os.path.join(*path_components0)[:-file_name_length - 1]
    if len(longest_prefix) > 0:
        longest_path_prefix = os.path.join(*longest_prefix)
        longest_prefix_length = len(longest_path_prefix) + 1
        if path_0[longest_prefix_length:] != '' and not root_comparison:
            path_0_components = path_components(path_0[longest_prefix_length:])
            if path_0_components[0] == ''and path_0_components[1] == ''and len(
                                        path_0[longest_prefix_length:]) > 20:
                path_0_components.insert(2, common_elmt)
                path_0 = os.path.join(*path_0_components)
            else:
                path_0 = path_0[longest_prefix_length:]
        elif not root_comparison:
            path_0 = common_elmt
        elif sys.platform.startswith('linux') and path_0 == '':
            path_0 = '/'
    return path_0