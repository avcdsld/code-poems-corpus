def repo_clone(from_name, to_name)
      Dir.chdir(tmp_repos_path) { `git clone #{from_name} #{to_name} 2>&1 > /dev/null` }
      repo_path(to_name)
    end