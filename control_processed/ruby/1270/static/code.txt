def withenv(hash, mode = :posix)
    saved = get_environment(mode)
    merge_environment(hash, mode)
    yield
  ensure
    if saved
      clear_environment(mode)
      merge_environment(saved, mode)
    end
  end