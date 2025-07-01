def precheck_app
      return true unless options[:run_precheck_before_submit]
      UI.message("Running precheck before submitting to review, if you'd like to disable this check you can set run_precheck_before_submit to false")

      if options[:submit_for_review]
        UI.message("Making sure we pass precheck 👮‍♀️ 👮 before we submit  🛫")
      else
        UI.message("Running precheck 👮‍♀️ 👮")
      end

      precheck_options = {
        default_rule_level: options[:precheck_default_rule_level],
        include_in_app_purchases: options[:precheck_include_in_app_purchases],
        app_identifier: options[:app_identifier],
        username: options[:username]
      }

      precheck_config = FastlaneCore::Configuration.create(Precheck::Options.available_options, precheck_options)
      Precheck.config = precheck_config

      precheck_success = true
      begin
        precheck_success = Precheck::Runner.new.run
      rescue => ex
        UI.error("fastlane precheck just tried to inspect your app's metadata for App Store guideline violations and ran into a problem. We're not sure what the problem was, but precheck failed to finished. You can run it in verbose mode if you want to see the whole error. We'll have a fix out soon 🚀")
        UI.verbose(ex.inspect)
        UI.verbose(ex.backtrace.join("\n"))
      end

      return precheck_success
    end