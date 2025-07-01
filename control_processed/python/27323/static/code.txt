def print_async_event(self, suffix, event):
        '''
        Print all of the events with the prefix 'tag'
        '''
        if not isinstance(event, dict):
            return

        # if we are "quiet", don't print
        if self.opts.get('quiet', False):
            return

        # some suffixes we don't want to print
        if suffix in ('new',):
            return

        try:
            outputter = self.opts.get('output', event.get('outputter', None) or event.get('return').get('outputter'))
        except AttributeError:
            outputter = None

        # if this is a ret, we have our own set of rules
        if suffix == 'ret':
            # Check if outputter was passed in the return data. If this is the case,
            # then the return data will be a dict two keys: 'data' and 'outputter'
            if isinstance(event.get('return'), dict) \
                    and set(event['return']) == set(('data', 'outputter')):
                event_data = event['return']['data']
                outputter = event['return']['outputter']
            else:
                event_data = event['return']
        else:
            event_data = {'suffix': suffix, 'event': event}

        salt.output.display_output(event_data, outputter, self.opts)