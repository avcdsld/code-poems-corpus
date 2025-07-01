def get_account(self, portfolio_cookie: str, account_cookie: str):
        """直接从二级目录拿到account

        Arguments:
            portfolio_cookie {str} -- [description]
            account_cookie {str} -- [description]

        Returns:
            [type] -- [description]
        """

        try:
            return self.portfolio_list[portfolio_cookie][account_cookie]
        except:
            return None