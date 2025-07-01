def start
      check_ruby_verison
      check_default_handlers

      begin
        Bundler.require
      rescue Bundler::GemfileNotFound
        say I18n.t("lita.cli.no_gemfile_warning"), :red
        abort
      end

      Lita.run(options[:config])
    end