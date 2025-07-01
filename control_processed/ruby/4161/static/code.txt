def on_event(event_type, target, extra = nil)
      case event_type
      when :error
        say_status :error, target, :red
        shell.say extra, :red if options['verbose'] || options['bail']

        raise 'Build error' if options['bail']
      when :deleted
        say_status :remove, target, :green
      when :created
        say_status :create, target, :green
      when :identical
        say_status :identical, target, :blue
      when :skipped
        say_status :skipped, target, :blue
      when :updated
        say_status :updated, target, :yellow
      else
        say_status event_type, extra, :blue
      end
    end