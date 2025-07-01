def copyMakeBorder(src, top, bot, left, right, border_type=cv2.BORDER_CONSTANT, value=0):
    """Pad image border
    Wrapper for cv2.copyMakeBorder that uses mx.nd.NDArray

    Parameters
    ----------
    src : NDArray
        Image in (width, height, channels).
        Others are the same with cv2.copyMakeBorder

    Returns
    -------
    img : NDArray
        padded image
    """
    hdl = NDArrayHandle()
    check_call(_LIB.MXCVcopyMakeBorder(src.handle, ctypes.c_int(top), ctypes.c_int(bot),
                                       ctypes.c_int(left), ctypes.c_int(right),
                                       ctypes.c_int(border_type), ctypes.c_double(value),
                                       ctypes.byref(hdl)))
    return mx.nd.NDArray(hdl)