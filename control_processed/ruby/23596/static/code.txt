def commands
      @commands ||= if @options[:except]
        @all_commands.reject{ |command| @options[:except].include?(command.label) }
      elsif @options[:only]
        @all_commands.select{ |command| @options[:only].include?(command.label) }
      else
        @all_commands
      end
    end