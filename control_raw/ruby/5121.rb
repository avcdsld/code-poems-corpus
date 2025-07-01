def say(message = '', options = {})
      message = message.to_s
      return if message.empty?

      statement = Statement.new(self, options)
      statement.call(message)
    end