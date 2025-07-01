def load_extensions
      configuration = TrustyCms::Application.config
      @observer ||= DependenciesObserver.new(configuration).observe(::ActiveSupport::Dependencies)
      self.extensions = configuration.enabled_extensions.map { |ext| load_extension(ext) }.compact
    end