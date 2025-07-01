def buy_close(id_or_ins, amount, price=None, style=None, close_today=False):
    """
    平卖仓

    :param id_or_ins: 下单标的物
    :type id_or_ins: :class:`~Instrument` object | `str` | List[:class:`~Instrument`] | List[`str`]

    :param int amount: 下单手数

    :param float price: 下单价格，默认为None，表示 :class:`~MarketOrder`, 此参数主要用于简化 `style` 参数。

    :param style: 下单类型, 默认是市价单。目前支持的订单类型有 :class:`~LimitOrder` 和 :class:`~MarketOrder`
    :type style: `OrderStyle` object

    :param bool close_today: 是否指定发平今仓单，默认为False，发送平仓单

    :return: :class:`~Order` object | list[:class:`~Order`] | None

    :example:

    .. code-block:: python

        #市价单将现有IF1603空仓买入平仓2张：
        buy_close('IF1603', 2)
    """
    position_effect = POSITION_EFFECT.CLOSE_TODAY if close_today else POSITION_EFFECT.CLOSE
    return order(id_or_ins, amount, SIDE.BUY, position_effect, cal_style(price, style))