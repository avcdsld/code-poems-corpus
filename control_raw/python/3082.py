def open_mask(fn:PathOrStr, div=False, convert_mode='L', after_open:Callable=None)->ImageSegment:
    "Return `ImageSegment` object create from mask in file `fn`. If `div`, divides pixel values by 255."
    return open_image(fn, div=div, convert_mode=convert_mode, cls=ImageSegment, after_open=after_open)