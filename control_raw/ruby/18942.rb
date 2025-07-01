def versions(constraints, elm_version, should_update, only_update)
      if repository.cloned? &&
         !repository.fetched &&
         should_update &&
         (!only_update || only_update == package_name)
        # Get updates from upstream
        Logger.arrow "Getting updates for: #{package_name.bold}"
        repository.fetch
      end

      case @branch
      when Branch::Just
        [identifier.version(fetch(@branch.ref))]
      when Branch::Nothing
        matching_versions constraints, elm_version
      end
    end