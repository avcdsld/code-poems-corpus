def get_fn_link(ft)->str:
    "Return function link to notebook documentation of `ft`. Private functions link to source code"
    ft = getattr(ft, '__func__', ft)
    anchor = strip_fastai(get_anchor(ft))
    module_name = strip_fastai(get_module_name(ft))
    base = '' if use_relative_links else FASTAI_DOCS
    return f'{base}/{module_name}.html#{anchor}'