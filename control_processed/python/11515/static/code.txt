def get_bar(self, code, time):
        """
        获取一个bar的数据
        返回一个series
        如果不存在,raise ValueError
        """
        try:
            return self.data.loc[(pd.Timestamp(time), code)]
        except:
            raise ValueError(
                'DATASTRUCT CURRENTLY CANNOT FIND THIS BAR WITH {} {}'.format(
                    code,
                    time
                )
            )