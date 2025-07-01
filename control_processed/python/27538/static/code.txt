def populate_client_cache(self, low):
        '''
        Populate the client cache with an instance of the specified type
        '''
        reaction_type = low['state']
        if reaction_type not in self.client_cache:
            log.debug('Reactor is populating %s client cache', reaction_type)
            if reaction_type in ('runner', 'wheel'):
                # Reaction types that run locally on the master want the full
                # opts passed.
                self.client_cache[reaction_type] = \
                    self.reaction_class[reaction_type](self.opts)
                # The len() function will cause the module functions to load if
                # they aren't already loaded. We want to load them so that the
                # spawned threads don't need to load them. Loading in the
                # spawned threads creates race conditions such as sometimes not
                # finding the required function because another thread is in
                # the middle of loading the functions.
                len(self.client_cache[reaction_type].functions)
            else:
                # Reactions which use remote pubs only need the conf file when
                # instantiating a client instance.
                self.client_cache[reaction_type] = \
                    self.reaction_class[reaction_type](self.opts['conf_file'])