def bar_amplitude(self):
        "返回bar振幅"
        res = (self.high - self.low) / self.low
        res.name = 'bar_amplitude'
        return res