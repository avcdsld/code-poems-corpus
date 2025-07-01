def _websocket_mask_python(mask: bytes, data: bytes) -> bytes:
    """Websocket masking function.

    `mask` is a `bytes` object of length 4; `data` is a `bytes` object of any length.
    Returns a `bytes` object of the same length as `data` with the mask applied
    as specified in section 5.3 of RFC 6455.

    This pure-python implementation may be replaced by an optimized version when available.
    """
    mask_arr = array.array("B", mask)
    unmasked_arr = array.array("B", data)
    for i in range(len(data)):
        unmasked_arr[i] = unmasked_arr[i] ^ mask_arr[i % 4]
    return unmasked_arr.tobytes()