def margin_rate(self):
        """
        [float] 合约最低保证金率（期货专用）
        """
        try:
            return self.__dict__["margin_rate"]
        except (KeyError, ValueError):
            raise AttributeError(
                "Instrument(order_book_id={}) has no attribute 'margin_rate' ".format(self.order_book_id)
            )