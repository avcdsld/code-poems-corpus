def get_data(self, df):
        """Returns the chart data"""
        chart_data = []
        if len(self.groupby) > 0:
            groups = df.groupby(self.groupby)
        else:
            groups = [((), df)]
        for keys, data in groups:
            chart_data.extend([{
                'key': self.labelify(keys, column),
                'values': data[column].tolist()}
                for column in self.columns])
        return chart_data