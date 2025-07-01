def standard_rake_options
      sort_options(
        [
          ['--all', '-A',
            "Show all tasks, even uncommented ones",
            lambda { |value|
              options.show_all_tasks = value
            }
          ],
          ['--backtrace=[OUT]',
            "Enable full backtrace.  OUT can be stderr (default) or stdout.",
            lambda { |value|
              options.backtrace = true
              select_trace_output(options, 'backtrace', value)
            }
          ],
          ['--comments',
            "Show commented tasks only",
            lambda { |value|
              options.show_all_tasks = !value
            }
          ],
          ['--describe', '-D [PATTERN]',
            "Describe the tasks (matching optional PATTERN), then exit.",
            lambda { |value|
              select_tasks_to_show(options, :describe, value)
            }
          ],
          ['--dry-run', '-n',
            "Do a dry run without executing actions.",
            lambda { |value|
              Rake.verbose(true)
              Rake.nowrite(true)
              options.dryrun = true
              options.trace = true
            }
          ],
          ['--execute', '-e CODE',
            "Execute some Ruby code and exit.",
            lambda { |value|
              eval(value)
              exit
            }
          ],
          ['--execute-print', '-p CODE',
            "Execute some Ruby code, print the result, then exit.",
            lambda { |value|
              puts eval(value)
              exit
            }
          ],
          ['--execute-continue',  '-E CODE',
            "Execute some Ruby code, " +
            "then continue with normal task processing.",
            lambda { |value| eval(value) }
          ],
          ['--jobs',  '-j [NUMBER]',
            "Specifies the maximum number of tasks to execute in parallel. " +
            "(default is 2)",
            lambda { |value|
              options.thread_pool_size = [(value || 2).to_i, 2].max
            }
          ],
          ['--job-stats [LEVEL]',
            "Display job statistics. " +
            "LEVEL=history displays a complete job list",
            lambda { |value|
              if value =~ /^history/i
                options.job_stats = :history
              else
                options.job_stats = true
              end
            }
          ],
          ['--libdir', '-I LIBDIR',
            "Include LIBDIR in the search path for required modules.",
            lambda { |value| $:.push(value) }
          ],
          ['--multitask', '-m',
            "Treat all tasks as multitasks.",
            lambda { |value| options.always_multitask = true }
          ],
          ['--no-search', '--nosearch',
            '-N', "Do not search parent directories for the Rakefile.",
            lambda { |value| options.nosearch = true }
          ],
          ['--prereqs', '-P',
            "Display the tasks and dependencies, then exit.",
            lambda { |value| options.show_prereqs = true }
          ],
          ['--quiet', '-q',
            "Do not log messages to standard output.",
            lambda { |value| Rake.verbose(false) }
          ],
          ['--rakefile', '-f [FILE]',
            "Use FILE as the rakefile.",
            lambda { |value|
              value ||= ''
              @rakefiles.clear
              @rakefiles << value
            }
          ],
          ['--rakelibdir', '--rakelib', '-R RAKELIBDIR',
            "Auto-import any .rake files in RAKELIBDIR. " +
            "(default is 'rakelib')",
            lambda { |value|
              options.rakelib = value.split(File::PATH_SEPARATOR)
            }
          ],
          ['--require', '-r MODULE',
            "Require MODULE before executing rakefile.",
            lambda { |value|
              begin
                require value
              rescue LoadError => ex
                begin
                  rake_require value
                rescue LoadError
                  raise ex
                end
              end
            }
          ],
          ['--rules',
            "Trace the rules resolution.",
            lambda { |value| options.trace_rules = true }
          ],
          ['--silent', '-s',
            "Like --quiet, but also suppresses the " +
            "'in directory' announcement.",
            lambda { |value|
              Rake.verbose(false)
              options.silent = true
            }
          ],
          ['--suppress-backtrace PATTERN',
            "Suppress backtrace lines matching regexp PATTERN. " +
            "Ignored if --trace is on.",
            lambda { |value|
              options.suppress_backtrace_pattern = Regexp.new(value)
            }
          ],
          ['--system',  '-g',
            "Using system wide (global) rakefiles " +
            "(usually '~/.rake/*.rake').",
            lambda { |value| options.load_system = true }
          ],
          ['--no-system', '--nosystem', '-G',
            "Use standard project Rakefile search paths, " +
            "ignore system wide rakefiles.",
            lambda { |value| options.ignore_system = true }
          ],
          ['--tasks', '-T [PATTERN]',
            "Display the tasks (matching optional PATTERN) " +
            "with descriptions, then exit.",
            lambda { |value|
              select_tasks_to_show(options, :tasks, value)
            }
          ],
          ['--trace=[OUT]', '-t',
            "Turn on invoke/execute tracing, enable full backtrace. " +
            "OUT can be stderr (default) or stdout.",
            lambda { |value|
              options.trace = true
              options.backtrace = true
              select_trace_output(options, 'trace', value)
              Rake.verbose(true)
            }
          ],
          ['--verbose', '-v',
            "Log message to standard output.",
            lambda { |value| Rake.verbose(true) }
          ],
          ['--version', '-V',
            "Display the program version.",
            lambda { |value|
              puts "rake, version #{RAKEVERSION}"
              exit
            }
          ],
          ['--where', '-W [PATTERN]',
            "Describe the tasks (matching optional PATTERN), then exit.",
            lambda { |value|
              select_tasks_to_show(options, :lines, value)
              options.show_all_tasks = true
            }
          ],
          ['--no-deprecation-warnings', '-X',
            "Disable the deprecation warnings.",
            lambda { |value|
              options.ignore_deprecate = true
            }
          ],
        ])
    end