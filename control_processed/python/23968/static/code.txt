def format_graylog_v0(self, record):
        '''
        Graylog 'raw' format is essentially the raw record, minimally munged to provide
        the bare minimum that td-agent requires to accept and route the event.  This is
        well suited to a config where the client td-agents log directly to Graylog.
        '''
        message_dict = {
            'message': record.getMessage(),
            'timestamp': self.formatTime(record),
            # Graylog uses syslog levels, not whatever it is Python does...
            'level': syslog_levels.get(record.levelname, 'ALERT'),
            'tag': self.tag
        }

        if record.exc_info:
            exc_info = self.formatException(record.exc_info)
            message_dict.update({'full_message': exc_info})

        # Add any extra attributes to the message field
        for key, value in six.iteritems(record.__dict__):
            if key in ('args', 'asctime', 'bracketlevel', 'bracketname', 'bracketprocess',
                       'created', 'exc_info', 'exc_text', 'id', 'levelname', 'levelno', 'msecs',
                       'msecs', 'message', 'msg', 'relativeCreated', 'version'):
                # These are already handled above or explicitly pruned.
                continue

            if isinstance(value, (six.string_types, bool, dict, float, int, list, types.NoneType)):  # pylint: disable=W1699
                val = value
            else:
                val = repr(value)
            message_dict.update({'{0}'.format(key): val})
        return message_dict