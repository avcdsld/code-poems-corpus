def pivot(self, column_):
        """增加对于多列的支持"""
        if isinstance(column_, str):
            try:
                return self.data.reset_index().pivot(
                    index='datetime',
                    columns='code',
                    values=column_
                )
            except:
                return self.data.reset_index().pivot(
                    index='date',
                    columns='code',
                    values=column_
                )
        elif isinstance(column_, list):
            try:
                return self.data.reset_index().pivot_table(
                    index='datetime',
                    columns='code',
                    values=column_
                )
            except:
                return self.data.reset_index().pivot_table(
                    index='date',
                    columns='code',
                    values=column_
                )