def folder_source(path, folder):
    """
    Returns the filenames and labels for a folder within a path
    
    Returns:
    -------
    fnames: a list of the filenames within `folder`
    all_lbls: a list of all of the labels in `folder`, where the # of labels is determined by the # of directories within `folder`
    lbl_arr: a numpy array of the label indices in `all_lbls`
    """
    fnames, lbls, all_lbls = read_dirs(path, folder)
    lbl2idx = {lbl:idx for idx,lbl in enumerate(all_lbls)}
    idxs = [lbl2idx[lbl] for lbl in lbls]
    lbl_arr = np.array(idxs, dtype=int)
    return fnames, lbl_arr, all_lbls