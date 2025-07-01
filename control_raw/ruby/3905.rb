def delete_all
      start do |pop3|
        unless pop3.mails.empty?
          pop3.delete_all
          pop3.finish
        end
      end
    end