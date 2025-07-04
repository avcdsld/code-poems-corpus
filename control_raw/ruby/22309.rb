def create(type = :session, attributes)
      case type
        when :session
          if attributes && attributes[:fee_ids] && attributes[:fee_ids].is_a?(Array)
            attributes[:fee_ids] = attributes[:fee_ids].join(',')
          end
          response = @client.get('request_session_token', attributes)
          JSON.parse(response.body)
        when :eui
          attributes[:token_type] = 'eui'
          response = @client.post('token_auths/', attributes)
          JSON.parse(response.body)
        when :card
          attributes[:token_type] = 'card'
          response = @client.post('token_auths/', attributes)
          JSON.parse(response.body)
        when :approve
          attributes[:token_type] = '4'
          response = @client.post('token_auths/', attributes)
          JSON.parse(response.body)
      end
    end