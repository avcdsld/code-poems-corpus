def lint
      return if target_files.empty?

      bin = textlint_path
      result_json = run_textlint(bin, target_files)
      errors = parse(result_json)
      send_comment(errors)
    end