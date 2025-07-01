def exchangebill(self):
        """
        默认提供最近30天的交割单, 通常只能返回查询日期内最新的 90 天数据。
        :return:
        """
        # TODO 目前仅在 华泰子类 中实现
        start_date, end_date = helpers.get_30_date()
        return self.get_exchangebill(start_date, end_date)