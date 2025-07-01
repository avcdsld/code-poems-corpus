def load_reporter_class(reporter_name)
      HamlLint::Reporter.const_get("#{reporter_name}Reporter")
    rescue NameError
      raise HamlLint::Exceptions::InvalidCLIOption,
            "#{reporter_name}Reporter does not exist"
    end