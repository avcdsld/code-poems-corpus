def parse(args)
      args = build_opts(args)

      OptionParser.new do |opts|
        opts.banner = 'Usage: undercover [options]'

        opts.on_tail('-h', '--help', 'Prints this help') do
          puts(opts)
          exit
        end

        opts.on_tail('--version', 'Show version') do
          puts VERSION
          exit
        end

        lcov_path_option(opts)
        project_path_option(opts)
        git_dir_option(opts)
        compare_option(opts)
        ruby_syntax_option(opts)
        # TODO: parse dem other options and assign to self
        # --quiet (skip progress bar)
        # --exit-status (do not print report, just exit)
      end.parse(args)

      guess_lcov_path unless lcov
      self
    end