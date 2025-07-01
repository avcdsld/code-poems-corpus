def _load_model(ptr, length):
    """
    Internal function used by the module,
    unpickle a model from a buffer specified by ptr, length
    Arguments:
        ptr: ctypes.POINTER(ctypes._char)
            pointer to the memory region of buffer
        length: int
            the length of buffer
    """
    data = (ctypes.c_char * length).from_address(ctypes.addressof(ptr.contents))
    return pickle.loads(data.raw)