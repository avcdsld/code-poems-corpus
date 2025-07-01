def rename_page(page, rename, commit = {})
      return false if page.nil?
      return false if rename.nil? or rename.empty?

      (target_dir, target_name) = ::File.split(rename)
      (source_dir, source_name) = ::File.split(page.path)
      source_name               = page.filename_stripped

      # File.split gives us relative paths with ".", commiter.add_to_index doesn't like that.
      target_dir                = '' if target_dir == '.'
      source_dir                = '' if source_dir == '.'
      target_dir                = target_dir.gsub(/^\//, '')

      # if the rename is a NOOP, abort
      if source_dir == target_dir and source_name == target_name
        return false
      end

      multi_commit = !!commit[:committer]
      committer    = multi_commit ? commit[:committer] : Committer.new(self, commit)

      committer.delete(page.path)
      committer.add_to_index(target_dir, target_name, page.format, page.raw_data)

      committer.after_commit do |index, _sha|
        @access.refresh
        index.update_working_dir(source_dir, source_name, page.format)
        index.update_working_dir(target_dir, target_name, page.format)
      end

      multi_commit ? committer : committer.commit
    end