def fail(*failures, **options)
      sticky = options.fetch(:sticky, false)
      file = options.fetch(:file, nil)
      line = options.fetch(:line, nil)

      failures.flatten.each do |failure|
        next if should_ignore_violation(failure)
        @errors << Violation.new(failure, sticky, file, line) if failure
      end
    end