def check_order_triggers(self, current_price):
        """
        Given an order and a trade event, return a tuple of
        (stop_reached, limit_reached).
        For market orders, will return (False, False).
        For stop orders, limit_reached will always be False.
        For limit orders, stop_reached will always be False.
        For stop limit orders a Boolean is returned to flag
        that the stop has been reached.

        Orders that have been triggered already (price targets reached),
        the order's current values are returned.
        """
        if self.triggered:
            return (self.stop_reached, self.limit_reached, False)

        stop_reached = False
        limit_reached = False
        sl_stop_reached = False

        order_type = 0

        if self.amount > 0:
            order_type |= BUY
        else:
            order_type |= SELL

        if self.stop is not None:
            order_type |= STOP

        if self.limit is not None:
            order_type |= LIMIT

        if order_type == BUY | STOP | LIMIT:
            if current_price >= self.stop:
                sl_stop_reached = True
                if current_price <= self.limit:
                    limit_reached = True
        elif order_type == SELL | STOP | LIMIT:
            if current_price <= self.stop:
                sl_stop_reached = True
                if current_price >= self.limit:
                    limit_reached = True
        elif order_type == BUY | STOP:
            if current_price >= self.stop:
                stop_reached = True
        elif order_type == SELL | STOP:
            if current_price <= self.stop:
                stop_reached = True
        elif order_type == BUY | LIMIT:
            if current_price <= self.limit:
                limit_reached = True
        elif order_type == SELL | LIMIT:
            # This is a SELL LIMIT order
            if current_price >= self.limit:
                limit_reached = True

        return (stop_reached, limit_reached, sl_stop_reached)