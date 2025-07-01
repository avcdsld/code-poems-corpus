def get_future_contracts(underlying_symbol):
    """
    获取某一期货品种在策略当前日期的可交易合约order_book_id列表。按照到期月份，下标从小到大排列，返回列表中第一个合约对应的就是该品种的近月合约。

    :param str underlying_symbol: 期货合约品种，例如沪深300股指期货为'IF'

    :return: list[`str`]

    :example:

    获取某一天的主力合约代码（策略当前日期是20161201）:

        ..  code-block:: python

            [In]
            logger.info(get_future_contracts('IF'))
            [Out]
            ['IF1612', 'IF1701', 'IF1703', 'IF1706']
    """
    env = Environment.get_instance()
    return env.data_proxy.get_future_contracts(underlying_symbol, env.trading_dt)