def lbmethods(self):
        '''
        List all the load balancer methods
        '''
        methods = self.bigIP.LocalLB.Pool.typefactory.create(
            'LocalLB.LBMethod'
        )
        return [method[0].split('_', 2)[-1] for method in methods]