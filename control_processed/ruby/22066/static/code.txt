def parse_options(args)
      opt_parser = OptionParser.new do |opts|
        # Set a banner, displayed at the top
        # of the help screen.
        opts.banner = 'Usage: k9 [options] [<filename.rb>]'
        # Define the options, and what they do
        options[:version] = false
        opts.on('-v', '--version', 'JRubyArt Version') do
          options[:version] = true
        end

        options[:install] = false
        opts.on('-i', '--install', 'Installs jruby-complete and examples') do
          options[:install] = true
        end

        options[:check] = false
        opts.on('-?', '--check', 'Prints configuration') do
          options[:check] = true
        end

        options[:app] = false
        opts.on('-a', '--app', 'Export as app NOT IMPLEMENTED YET') do
          options[:export] = true
        end

        options[:watch] = false
        opts.on('-w', '--watch', 'Watch/run the sketch') do
          options[:watch] = true
        end

        options[:run] = false
        opts.on('-r', '--run', 'Run the sketch') do
          options[:run] = true
        end

        options[:live] = false
        opts.on('-l', '--live', 'As above, with pry console bound to Processing.app') do
          options[:live] = true
        end

        options[:create] = false
        opts.on('-c', '--create', 'Create new outline sketch') do
          options[:create] = true
        end

        # This displays the help screen, all programs are
        # assumed to have this option.
        opts.on('-h', '--help', 'Display this screen') do
          puts opts
          exit
        end
      end
      @argc = opt_parser.parse(args)
      @filename = argc.shift
    end