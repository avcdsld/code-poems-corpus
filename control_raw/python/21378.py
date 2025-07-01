def sell_open_order_quantity(self):
        """
        [int] 卖方向挂单量
        """
        return sum(order.unfilled_quantity for order in self.open_orders if
                   order.side == SIDE.SELL and order.position_effect == POSITION_EFFECT.OPEN)