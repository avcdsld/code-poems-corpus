def profit_construct(self):
        """利润构成

        Returns:
            dict -- 利润构成表
        """

        return {
            'total_buyandsell':
            round(
                self.profit_money - self.total_commission - self.total_tax,
                2
            ),
            'total_tax':
            self.total_tax,
            'total_commission':
            self.total_commission,
            'total_profit':
            self.profit_money
        }