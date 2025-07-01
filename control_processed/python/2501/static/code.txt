def _url_params(size:str='>400*300', format:str='jpg') -> str:
    "Build Google Images Search Url params and return them as a string."
    _fmts = {'jpg':'ift:jpg','gif':'ift:gif','png':'ift:png','bmp':'ift:bmp', 'svg':'ift:svg','webp':'webp','ico':'ift:ico'}
    if size not in _img_sizes: 
        raise RuntimeError(f"""Unexpected size argument value: {size}.
                    See `widgets.image_downloader._img_sizes` for supported sizes.""") 
    if format not in _fmts: 
        raise RuntimeError(f"Unexpected image file format: {format}. Use jpg, gif, png, bmp, svg, webp, or ico.")
    return "&tbs=" + _img_sizes[size] + "," + _fmts[format]