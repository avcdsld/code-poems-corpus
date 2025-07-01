def QA_indicator_OSC(DataFrame, N=20, M=6):
    """变动速率线

    震荡量指标OSC，也叫变动速率线。属于超买超卖类指标,是从移动平均线原理派生出来的一种分析指标。

    它反应当日收盘价与一段时间内平均收盘价的差离值,从而测出股价的震荡幅度。

    按照移动平均线原理，根据OSC的值可推断价格的趋势，如果远离平均线，就很可能向平均线回归。
    """
    C = DataFrame['close']
    OS = (C - MA(C, N)) * 100
    MAOSC = EMA(OS, M)
    DICT = {'OSC': OS, 'MAOSC': MAOSC}

    return pd.DataFrame(DICT)