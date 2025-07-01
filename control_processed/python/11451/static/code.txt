def standartDeviation(self, series, start, limit):
        '''
        :type start: int
        :type limit: int
        :rtype: float
        '''
        return float(np.std(series[start:limit]))