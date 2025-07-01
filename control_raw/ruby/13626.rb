def fork_bare(path, options = {})
      default_options = {:bare => true, :shared => true}
      real_options = default_options.merge(options)
      Git.new(path).fs_mkdir('..')
      self.git.clone(real_options, self.path, path)
      Repo.new(path)
    end