def file_needs_update?(filename: nil)
      # looking for something like: FastlaneRunnerAPIVersion [0.9.1]
      regex_to_use = API_VERSION_REGEX

      source = File.join(self.source_swift_code_file_folder_path, "/#{filename}")
      target = File.join(self.target_swift_code_file_folder_path, "/#{filename}")

      # target doesn't have the file yet, so ya, I'd say it needs to be updated
      return true unless File.exist?(target)

      source_file_content = File.read(source)
      target_file_content = File.read(target)

      bundled_version = source_file_content.match(regex_to_use)[1]
      target_version = target_file_content.match(regex_to_use)[1]
      file_versions_are_different = bundled_version != target_version

      UI.verbose("#{filename} FastlaneRunnerAPIVersion (bundled/target): #{bundled_version}/#{target_version}")
      files_are_different = source_file_content != target_file_content

      if files_are_different && !file_versions_are_different
        UI.verbose("File versions are the same, but the two files are not equal, so that's a problem, setting needs update to 'true'")
      end

      needs_update = file_versions_are_different || files_are_different

      return needs_update
    end