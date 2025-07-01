def find(command, options = {}, &block)
      case command
      when Integer
        record(command)
      when Array
        command.map { |i| record(i) }
      when :all
        find_all(options, &block)
      when :first
        find_first(options)
      end
    end