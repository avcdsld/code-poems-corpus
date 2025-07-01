def preform(url, type, params = {}, &block)
      ActiveSupport::Notifications.instrument 'Seoshop', request: type, url: url, params: params do
        if connection.in_parallel?
          block.call
        else
          block.call.body
        end
      end
    end