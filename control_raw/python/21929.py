def competition_view_leaderboard(self, id, **kwargs):  # noqa: E501
        """VIew competition leaderboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.competition_view_leaderboard(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Competition name (required)
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.competition_view_leaderboard_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.competition_view_leaderboard_with_http_info(id, **kwargs)  # noqa: E501
            return data