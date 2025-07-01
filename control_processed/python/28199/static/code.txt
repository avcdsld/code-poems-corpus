def return_pub(self, ret):
        '''
        Return the data up to the master
        '''
        channel = salt.transport.client.ReqChannel.factory(self.opts, usage='salt_call')
        load = {'cmd': '_return', 'id': self.opts['id']}
        for key, value in six.iteritems(ret):
            load[key] = value
        try:
            channel.send(load)
        finally:
            channel.close()