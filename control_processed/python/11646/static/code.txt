def QA_fetch_index_min_adv(
        code,
        start, end=None,
        frequence='1min',
        if_drop_index=True,
        collections=DATABASE.index_min):
    '''
    '获取股票分钟线'
    :param code:
    :param start:
    :param end:
    :param frequence:
    :param if_drop_index:
    :param collections:
    :return:
    '''
    if frequence in ['1min', '1m']:
        frequence = '1min'
    elif frequence in ['5min', '5m']:
        frequence = '5min'
    elif frequence in ['15min', '15m']:
        frequence = '15min'
    elif frequence in ['30min', '30m']:
        frequence = '30min'
    elif frequence in ['60min', '60m']:
        frequence = '60min'

    # __data = [] 没有使用

    end = start if end is None else end
    if len(start) == 10:
        start = '{} 09:30:00'.format(start)
    if len(end) == 10:
        end = '{} 15:00:00'.format(end)

    # 🛠 todo 报告错误 如果开始时间 在 结束时间之后

    # if start == end:
    # 🛠 todo 如果相等，根据 frequence 获取开始时间的 时间段 QA_fetch_index_min_adv， 不支持start end是相等的
    #print("QA Error QA_fetch_index_min_adv parameter code=%s , start=%s, end=%s is equal, should have time span! " % (code, start, end))
    # return None

    res = QA_fetch_index_min(
        code, start, end, format='pd', frequence=frequence)
    if res is None:
        print("QA Error QA_fetch_index_min_adv parameter code=%s start=%s end=%s frequence=%s call QA_fetch_index_min return None" % (
            code, start, end, frequence))
    else:
        res_reset_index = res.set_index(
            ['datetime', 'code'], drop=if_drop_index)
        # if res_reset_index is None:
        #     print("QA Error QA_fetch_index_min_adv set index 'date, code' return None")
        return QA_DataStruct_Index_min(res_reset_index)