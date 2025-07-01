def set_defaults
      set_if_empty :karafka_role, :karafka
      set_if_empty :karafka_processes, 1
      set_if_empty :karafka_consumer_groups, []
      set_if_empty :karafka_default_hooks, -> { true }
      set_if_empty :karafka_env, -> { fetch(:karafka_env, fetch(:environment)) }
      set_if_empty :karafka_pid, -> { File.join(shared_path, 'tmp', 'pids', 'karafka.pid') }
    end