def await(timeout: Calabash::Wait.default_options[:timeout])
      timeout_message = lambda do |wait_options|
        "Timed out waiting for page #{self.class}: Waited #{wait_options[:timeout]} seconds for trait #{trait} to match a view"
      end

      cal.wait_for_view(trait, timeout: timeout, timeout_message: timeout_message)
    end