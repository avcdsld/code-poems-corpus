def QA_util_to_datetime(time):
    """
    字符串 '2018-01-01'  转变成 datatime 类型
    :param time: 字符串str -- 格式必须是 2018-01-01 ，长度10
    :return: 类型datetime.datatime
    """
    if len(str(time)) == 10:
        _time = '{} 00:00:00'.format(time)
    elif len(str(time)) == 19:
        _time = str(time)
    else:
        QA_util_log_info('WRONG DATETIME FORMAT {}'.format(time))
    return datetime.datetime.strptime(_time, '%Y-%m-%d %H:%M:%S')