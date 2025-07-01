def publish(self, load):
        '''
        This method sends out publications to the minions, it can only be used
        by the LocalClient.
        '''
        extra = load.get('kwargs', {})

        publisher_acl = salt.acl.PublisherACL(self.opts['publisher_acl_blacklist'])

        if publisher_acl.user_is_blacklisted(load['user']) or \
                publisher_acl.cmd_is_blacklisted(load['fun']):
            log.error(
                '%s does not have permissions to run %s. Please contact '
                'your local administrator if you believe this is in error.',
                load['user'], load['fun']
            )
            return {'error': {'name': 'AuthorizationError',
                              'message': 'Authorization error occurred.'}}

        # Retrieve the minions list
        delimiter = load.get('kwargs', {}).get('delimiter', DEFAULT_TARGET_DELIM)
        _res = self.ckminions.check_minions(
            load['tgt'],
            load.get('tgt_type', 'glob'),
            delimiter
        )
        minions = _res['minions']

        # Check for external auth calls and authenticate
        auth_type, err_name, key = self._prep_auth_info(extra)
        if auth_type == 'user':
            auth_check = self.loadauth.check_authentication(load, auth_type, key=key)
        else:
            auth_check = self.loadauth.check_authentication(extra, auth_type)

        # Setup authorization list variable and error information
        auth_list = auth_check.get('auth_list', [])
        error = auth_check.get('error')
        err_msg = 'Authentication failure of type "{0}" occurred.'.format(auth_type)

        if error:
            # Authentication error occurred: do not continue.
            log.warning(err_msg)
            return {'error': {'name': 'AuthenticationError',
                              'message': 'Authentication error occurred.'}}

        # All Token, Eauth, and non-root users must pass the authorization check
        if auth_type != 'user' or (auth_type == 'user' and auth_list):
            # Authorize the request
            authorized = self.ckminions.auth_check(
                auth_list,
                load['fun'],
                load['arg'],
                load['tgt'],
                load.get('tgt_type', 'glob'),
                minions=minions,
                # always accept find_job
                whitelist=['saltutil.find_job'],
            )

            if not authorized:
                # Authorization error occurred. Log warning and do not continue.
                log.warning(err_msg)
                return {'error': {'name': 'AuthorizationError',
                                  'message': 'Authorization error occurred.'}}

            # Perform some specific auth_type tasks after the authorization check
            if auth_type == 'token':
                username = auth_check.get('username')
                load['user'] = username
                log.debug('Minion tokenized user = "%s"', username)
            elif auth_type == 'eauth':
                # The username we are attempting to auth with
                load['user'] = self.loadauth.load_name(extra)

        # If we order masters (via a syndic), don't short circuit if no minions
        # are found
        if not self.opts.get('order_masters'):
            # Check for no minions
            if not minions:
                return {
                    'enc': 'clear',
                    'load': {
                        'jid': None,
                        'minions': minions
                    }
                }
        # Retrieve the jid
        if not load['jid']:
            fstr = '{0}.prep_jid'.format(self.opts['master_job_cache'])
            load['jid'] = self.mminion.returners[fstr](nocache=extra.get('nocache', False))
        self.event.fire_event({'minions': minions}, load['jid'])

        new_job_load = {
                'jid': load['jid'],
                'tgt_type': load['tgt_type'],
                'tgt': load['tgt'],
                'user': load['user'],
                'fun': load['fun'],
                'arg': salt.utils.args.parse_input(
                    load['arg'],
                    no_parse=load.get('no_parse', [])),
                'minions': minions,
            }

        # Announce the job on the event bus
        self.event.fire_event(new_job_load, 'new_job')  # old dup event
        self.event.fire_event(new_job_load, salt.utils.event.tagify([load['jid'], 'new'], 'job'))

        # Save the invocation information
        if self.opts['ext_job_cache']:
            try:
                fstr = '{0}.save_load'.format(self.opts['ext_job_cache'])
                self.mminion.returners[fstr](load['jid'], load)
            except KeyError:
                log.critical(
                    'The specified returner used for the external job cache '
                    '"%s" does not have a save_load function!',
                    self.opts['ext_job_cache']
                )
            except Exception:
                log.critical(
                    'The specified returner threw a stack trace:',
                    exc_info=True
                )

        # always write out to the master job cache
        try:
            fstr = '{0}.save_load'.format(self.opts['master_job_cache'])
            self.mminion.returners[fstr](load['jid'], load)
        except KeyError:
            log.critical(
                'The specified returner used for the master job cache '
                '"%s" does not have a save_load function!',
                self.opts['master_job_cache']
            )
        except Exception:
            log.critical(
                'The specified returner threw a stack trace:',
                exc_info=True
            )
        # Altering the contents of the publish load is serious!! Changes here
        # break compatibility with minion/master versions and even tiny
        # additions can have serious implications on the performance of the
        # publish commands.
        #
        # In short, check with Thomas Hatch before you even think about
        # touching this stuff, we can probably do what you want to do another
        # way that won't have a negative impact.
        pub_load = {
            'fun': load['fun'],
            'arg': salt.utils.args.parse_input(
                load['arg'],
                no_parse=load.get('no_parse', [])),
            'tgt': load['tgt'],
            'jid': load['jid'],
            'ret': load['ret'],
        }

        if 'id' in extra:
            pub_load['id'] = extra['id']
        if 'tgt_type' in load:
            pub_load['tgt_type'] = load['tgt_type']
        if 'to' in load:
            pub_load['to'] = load['to']

        if 'kwargs' in load:
            if 'ret_config' in load['kwargs']:
                pub_load['ret_config'] = load['kwargs'].get('ret_config')

            if 'metadata' in load['kwargs']:
                pub_load['metadata'] = load['kwargs'].get('metadata')

            if 'ret_kwargs' in load['kwargs']:
                pub_load['ret_kwargs'] = load['kwargs'].get('ret_kwargs')

        if 'user' in load:
            log.info(
                'User %s Published command %s with jid %s',
                load['user'], load['fun'], load['jid']
            )
            pub_load['user'] = load['user']
        else:
            log.info(
                'Published command %s with jid %s',
                load['fun'], load['jid']
            )
        log.debug('Published command details %s', pub_load)

        return {'ret': {
                    'jid': load['jid'],
                    'minions': minions
                    },
                'pub': pub_load
                }