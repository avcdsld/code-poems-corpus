def call
      return recipients unless mailable.respond_to?(:conversation)

      recipients.each_with_object([]) do |recipient, array|
        array << recipient if mailable.conversation.has_subscriber?(recipient)
      end
    end