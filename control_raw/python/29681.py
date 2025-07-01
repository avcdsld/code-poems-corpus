def process_presence_events(self, event_data, token, opts):
        '''
        Check if any minions have connected or dropped.
        Send a message to the client if they have.
        '''
        tag = event_data['tag']
        event_info = event_data['data']

        minions_detected = event_info['present']
        curr_minions = six.iterkeys(self.minions)

        changed = False

        # check if any connections were dropped
        dropped_minions = set(curr_minions) - set(minions_detected)

        for minion in dropped_minions:
            changed = True
            self.minions.pop(minion, None)

        # check if any new connections were made
        new_minions = set(minions_detected) - set(curr_minions)

        tgt = ','.join(new_minions)

        if tgt:
            changed = True
            client = salt.netapi.NetapiClient(opts)
            client.run(
                {
                    'fun': 'grains.items',
                    'tgt': tgt,
                    'expr_type': 'list',
                    'mode': 'client',
                    'client': 'local',
                    'asynchronous': 'local_async',
                    'token': token,
                })

        if changed:
            self.publish_minions()