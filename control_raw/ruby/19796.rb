def parse!(argv)
      command = nil
      arguments = nil
      # https://github.com/aws/aws-sdk-ruby/blob/v2.3.11/aws-sdk-core/lib/aws-sdk-core/plugins/regional_endpoint.rb#L18
      region_keys = %w(AWS_REGION AMAZON_REGION AWS_DEFAULT_REGION)
      options = { aws: { region: ENV.values_at(*region_keys).compact.first,
                  retry_limit: DEFAULT_OPTION_RETRY_LIMIT } }

      opt = ::OptionParser.new
      opt.summary_width = 65535
      set_usage!(opt)

      opt.on('-k', '--access-key ACCESS_KEY') {|v| options[:aws][:access_key_id]     = v }
      opt.on('-s', '--secret-key SECRET_KEY') {|v| options[:aws][:secret_access_key] = v }
      opt.on('-r', '--region REGION')         {|v| options[:aws][:region]            = v }
      opt.on('',   '--retry-limit LIMIT')     {|v| options[:aws][:retry_limit]       = v }

      opt.on('', '--profile PROFILE') do |v|
        options[:aws][:credentials] ||= {}
        options[:aws][:credentials][:profile_name] = v
      end

      opt.on('', '--credentials-path PATH') do |v|
        options[:aws][:credentials] ||= {}
        options[:aws][:credentials][:path] = v
      end

      plugin_exts = Kumogata2::Plugin.plugins.flat_map(&:ext).uniq
      opt.on(''  , '--output-format FORMAT', plugin_exts) do |v|
        options[:output_format] = v
      end

      opt.on('-p', '--parameters KEY_VALUES', Array) {|v| options[:parameters]              = v }
      opt.on('-j', '--json-parameters JSON')         {|v| options[:json_parameters]         = v }
      opt.on(''  , '--[no-]deletion-policy-retain')  {|v| options[:deletion_policy_retain]  = v }

      {
        disable_rollback: :boolean,
        timeout_in_minutes: Integer,
        notification_arns: Array,
        capabilities: Array,
        resource_types: Array,
        on_failure: nil,
        stack_policy_body: nil,
        stack_policy_url: nil,
        use_previous_template: :boolean,
        stack_policy_during_update_body: nil,
        stack_policy_during_update_url: nil,
        tags: Array,
      }.each do |key, type|
        opt_str = key.to_s.gsub('_', '-')
        opt_val = key.to_s.upcase

        case type
        when :boolean
          opt.on('', "--[no-]#{opt_str}") {|v| options[key] = v }
        when nil
          opt.on('', "--#{opt_str} #{opt_val}") {|v| options[key] = v }
        else
          opt.on('', "--#{opt_str} #{opt_val}", type) {|v| options[key] = v }
        end
      end

      opt.on(''  , '--result-log PATH')         {|v| options[:result_log]       = v }
      opt.on(''  , '--command-result-log PATH') {|v| options[:command]          = v }
      opt.on(''  , '--[no-]detach')             {|v| options[:detach]           = v }
      opt.on(''  , '--[no-]force')              {|v| options[:force]            = v }
      opt.on(''  , '--[no-]color')              {|v| options[:color]            = v }
      opt.on(''  , '--[no-]ignore-all-space')   {|v| options[:ignore_all_space] = v }
      opt.on(''  , '--[no-]debug')              {|v| options[:debug]            = v }

      opt.parse!

      unless (command = argv.shift)
        puts opt.help
        exit_parse!(1)
      end

      orig_command = command
      command = command.gsub('-', '_').to_sym
      command = find_command(command)

      unless command
        raise "Unknown command: #{orig_command}"
      end

      arguments = argv.dup
      validate_arguments(command, arguments)

      options = DEFAULT_OPTIONS.merge(options)
      options = Hashie::Mash.new(options)

      if options[:aws][:credentials]
        credentials = Aws::SharedCredentials.new(options[:aws][:credentials])
        options[:aws][:credentials] = credentials
      end

      Aws.config.update(options[:aws].dup)
      options = Hashie::Mash.new(options)

      String.colorize = options.color?
      Diffy::Diff.default_format = options.color? ? :color : :text

      if options.debug?
        Kumogata2::Logger.instance.set_debug(options.debug?)

        Aws.config.update(
          http_wire_trace: true,
          logger: Kumogata2::Logger.instance
        )
      end

      update_parameters(options)
      output = COMMANDS.fetch(command).fetch(:output, true)

      options.command = command
      options.arguments = arguments
      options.output_result = output

      [command, arguments, options, output]
    end