def modified_files(options)
      flags = '--cached' if options[:staged]
      refs = options[:refs]
      subcmd = options[:subcmd] || 'diff'

      `git #{subcmd} --name-only -z --diff-filter=ACMR --ignore-submodules=all #{flags} #{refs}`.
        split("\0").
        map(&:strip).
        reject(&:empty?).
        map { |relative_file| File.expand_path(relative_file) }
    end