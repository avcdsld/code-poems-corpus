def QA_util_code_tolist(code, auto_fill=True):
    """转换code==> list

    Arguments:
        code {[type]} -- [description]

    Keyword Arguments:
        auto_fill {bool} -- 是否自动补全(一般是用于股票/指数/etf等6位数,期货不适用) (default: {True})

    Returns:
        [list] -- [description]
    """

    if isinstance(code, str):
        if auto_fill:
            return [QA_util_code_tostr(code)]
        else:
            return [code]

    elif isinstance(code, list):
        if auto_fill:
            return [QA_util_code_tostr(item) for item in code]
        else:
            return [item for item in code]