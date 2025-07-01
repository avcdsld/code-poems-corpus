def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if the asset is in the restricted_list.
        """
        if self.restrictions.is_restricted(asset, algo_datetime):
            self.handle_violation(asset, amount, algo_datetime)