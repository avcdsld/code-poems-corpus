def QA_indicator_DMA(DataFrame, M1=10, M2=50, M3=10):
    """
    平均线差 DMA
    """
    CLOSE = DataFrame.close
    DDD = MA(CLOSE, M1) - MA(CLOSE, M2)
    AMA = MA(DDD, M3)
    return pd.DataFrame({
        'DDD': DDD, 'AMA': AMA
    })