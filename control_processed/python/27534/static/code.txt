def delete_reactor(self, tag):
        '''
        Delete a reactor
        '''
        reactors = self.list_all()
        for reactor in reactors:
            _tag = next(six.iterkeys(reactor))
            if _tag == tag:
                self.minion.opts['reactor'].remove(reactor)
                return {'status': True, 'comment': 'Reactor deleted.'}

        return {'status': False, 'comment': 'Reactor does not exists.'}