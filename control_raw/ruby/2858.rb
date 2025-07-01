def process_file(file, report)
      lints = collect_lints(file, linter_selector, config)
      lints.each { |lint| report.add_lint(lint) }
      report.finish_file(file, lints)
    end