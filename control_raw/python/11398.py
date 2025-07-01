def message(self):
        """portfolio 的cookie
        """
        return {
            'user_cookie': self.user_cookie,
            'portfolio_cookie': self.portfolio_cookie,
            'account_list': list(self.account_list),
            'init_cash': self.init_cash,
            'cash': self.cash,
            'history': self.history
        }