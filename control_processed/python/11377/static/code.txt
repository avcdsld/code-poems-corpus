def QA_util_future_to_tradedatetime(real_datetime):
    """输入是真实交易时间,返回按期货交易所规定的时间* 适用于tb/文华/博弈的转换

    Arguments:
        real_datetime {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if len(str(real_datetime)) >= 19:
        dt = datetime.datetime.strptime(
            str(real_datetime)[0:19],
            '%Y-%m-%d %H:%M:%S'
        )
        return dt if dt.time(
        ) < datetime.time(21,
                          0) else QA_util_get_next_datetime(dt,
                                                            1)
    elif len(str(real_datetime)) == 16:
        dt = datetime.datetime.strptime(
            str(real_datetime)[0:16],
            '%Y-%m-%d %H:%M'
        )
        return dt if dt.time(
        ) < datetime.time(21,
                          0) else QA_util_get_next_datetime(dt,
                                                            1)