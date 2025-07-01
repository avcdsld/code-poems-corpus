def run_for_device_and_language(language, locale, device, launch_arguments, retries = 0)
      return launch_one_at_a_time(language, locale, device, launch_arguments)
    rescue => ex
      UI.error(ex.to_s) # show the reason for failure to the user, but still maybe retry

      if retries < launcher_config.number_of_retries
        UI.important("Tests failed, re-trying #{retries + 1} out of #{launcher_config.number_of_retries + 1} times")
        run_for_device_and_language(language, locale, device, launch_arguments, retries + 1)
      else
        UI.error("Backtrace:\n\t#{ex.backtrace.join("\n\t")}") if FastlaneCore::Globals.verbose?
        self.collected_errors << ex
        raise ex if launcher_config.stop_after_first_error
        return false # for the results
      end
    end