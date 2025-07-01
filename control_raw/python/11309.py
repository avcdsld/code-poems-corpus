def current_hold_price(self):
        """计算目前持仓的成本  用于模拟盘和实盘查询

        Returns:
            [type] -- [description]
        """
        
        def weights(x):
            n=len(x)
            res=1
            while res>0 or res<0:
                res=sum(x[:n]['amount'])
                n=n-1
            
            x=x[n+1:]     
            
            if sum(x['amount']) != 0:
                return np.average(
                    x['price'],
                    weights=x['amount'],
                    returned=True
                )
            else:
                return np.nan
        return self.history_table.set_index(
            'datetime',
            drop=False
        ).sort_index().groupby('code').apply(weights).dropna()