def process_minion_update(self, event_data):
        '''
        Associate grains data with a minion and publish minion update
        '''
        tag = event_data['tag']
        event_info = event_data['data']

        mid = tag.split('/')[-1]

        if not self.minions.get(mid, None):
            self.minions[mid] = {}

        minion = self.minions[mid]

        minion.update({'grains': event_info['return']})
        log.debug("In process minion grains update with minions=%s", self.minions)
        self.publish_minions()