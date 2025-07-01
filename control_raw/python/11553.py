def QA_fetch_get_stock_adj(code, end=''):
    """获取股票的复权因子
    
    Arguments:
        code {[type]} -- [description]
    
    Keyword Arguments:
        end {str} -- [description] (default: {''})
    
    Returns:
        [type] -- [description]
    """

    pro = get_pro()
    adj = pro.adj_factor(ts_code=code, trade_date=end)
    return adj