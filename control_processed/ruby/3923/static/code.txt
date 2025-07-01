def validate_options(options)
        options = options ? Hash[options] : {}
        options[:mailbox] ||= 'INBOX'
        options[:count]   ||= 10
        options[:order]   ||= :asc
        options[:what]    ||= :first
        options[:keys]    ||= 'ALL'
        options[:uid]     ||= nil
        options[:delete_after_find] ||= false
        options[:mailbox] = Net::IMAP.encode_utf7(options[:mailbox])
        options[:read_only] ||= false

        options
      end