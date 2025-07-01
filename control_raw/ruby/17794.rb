def perform(provider_sym, method_sym, provider_options={})
      tasks << @task_class.new(providers[provider_sym], method_sym, provider_options)
    end