def parse_generic_options(args)
      a = args.dup
      arguments = []
      options = {}

      until a.empty?
        arg = a.shift
        case arg
        when /\A--.+=/
          _, option, value = arg.match(/\A--(.+)=(.+)\Z/).to_a
          update_options(option, value, options)
        when /\A--.+/
          if a[0].nil? || a[0].to_s.start_with?("--")
            # Current option is a boolean
            update_options(arg, true, options)
          else
            # Take value from next
            update_options(arg, a.shift, options)
          end
        else
          arguments << arg
        end
      end

      [options, arguments]
    end