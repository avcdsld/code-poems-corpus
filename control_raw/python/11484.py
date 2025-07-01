def shadow_calc(data):
    """计算上下影线

    Arguments:
        data {DataStruct.slice} -- 输入的是一个行情切片

    Returns:
        up_shadow {float} -- 上影线
        down_shdow {float} -- 下影线
        entity {float} -- 实体部分
        date {str} -- 时间
        code {str} -- 代码
    """

    up_shadow = abs(data.high - (max(data.open, data.close)))
    down_shadow = abs(data.low - (min(data.open, data.close)))
    entity = abs(data.open - data.close)
    towards = True if data.open < data.close else False
    print('=' * 15)
    print('up_shadow : {}'.format(up_shadow))
    print('down_shadow : {}'.format(down_shadow))
    print('entity: {}'.format(entity))
    print('towards : {}'.format(towards))
    return up_shadow, down_shadow, entity, data.date, data.code