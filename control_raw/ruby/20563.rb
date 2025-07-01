def send_message(message)
      response = self.class.post(@api.send_message_config[:url],
        :query => { :auth_token => @token },
        :body  => {
          :room_id => room_id,
          :message => message,
        }.send(@api.send_config[:body_format]),
        :headers => @api.headers
      )

      ErrorHandler.response_code_to_exception_for :room, room_id, response
      true
    end