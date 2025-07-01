def find(options=nil, &block)
      options = validate_options(options)

      start do |imap|
        options[:read_only] ? imap.examine(options[:mailbox]) : imap.select(options[:mailbox])
        uids = imap.uid_search(options[:keys], options[:search_charset])
        uids.reverse! if options[:what].to_sym == :last
        uids = uids.first(options[:count]) if options[:count].is_a?(Integer)
        uids.reverse! if (options[:what].to_sym == :last && options[:order].to_sym == :asc) ||
                                (options[:what].to_sym != :last && options[:order].to_sym == :desc)

        if block_given?
          uids.each do |uid|
            uid = options[:uid].to_i unless options[:uid].nil?
            fetchdata = imap.uid_fetch(uid, ['RFC822', 'FLAGS'])[0]
            new_message = Mail.new(fetchdata.attr['RFC822'])
            new_message.mark_for_delete = true if options[:delete_after_find]

            if block.arity == 4
              yield new_message, imap, uid, fetchdata.attr['FLAGS']
            elsif block.arity == 3
              yield new_message, imap, uid
            else
              yield new_message
            end

            imap.uid_store(uid, "+FLAGS", [Net::IMAP::DELETED]) if options[:delete_after_find] && new_message.is_marked_for_delete?
            break unless options[:uid].nil?
          end
          imap.expunge if options[:delete_after_find]
        else
          emails = []
          uids.each do |uid|
            uid = options[:uid].to_i unless options[:uid].nil?
            fetchdata = imap.uid_fetch(uid, ['RFC822'])[0]
            emails << Mail.new(fetchdata.attr['RFC822'])
            imap.uid_store(uid, "+FLAGS", [Net::IMAP::DELETED]) if options[:delete_after_find]
            break unless options[:uid].nil?
          end
          imap.expunge if options[:delete_after_find]
          emails.size == 1 && options[:count] == 1 ? emails.first : emails
        end
      end
    end