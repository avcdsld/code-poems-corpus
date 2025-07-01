def register_event(self):
        """
        注册事件
        """
        event_bus = Environment.get_instance().event_bus
        event_bus.prepend_listener(EVENT.PRE_BEFORE_TRADING, self._pre_before_trading)
        event_bus.prepend_listener(EVENT.POST_SETTLEMENT, self._post_settlement)