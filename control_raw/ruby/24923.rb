def to_lcov_info(cov, out: "", test_name: nil)
      out << "TN:#{ test_name }\n"
      cov.each do |path, runs|
        out << "SF:#{ path }\n"

        # function coverage
        if runs.is_a?(Hash) && runs[:methods]
          total = covered = 0
          runs[:methods].each do |(klass, name, lineno), run|
            out << "FN:#{ lineno },#{ klass }##{ name }\n"
            total += 1
            covered += 1 if run > 0
          end
          out << "FNF:#{ total }\n"
          out << "FNF:#{ covered }\n"
          runs[:methods].each do |(klass, name, _), run|
            out << "FNDA:#{ run },#{ klass }##{ name }\n"
          end
        end

        # line coverage
        if runs.is_a?(Array) || (runs.is_a?(Hash) && runs[:lines])
          total = covered = 0
          lines = runs.is_a?(Array) ? runs : runs[:lines]
          lines.each_with_index do |run, lineno|
            next unless run
            out << "DA:#{ lineno + 1 },#{ run }\n"
            total += 1
            covered += 1 if run > 0
          end
          out << "LF:#{ total }\n"
          out << "LH:#{ covered }\n"
        end

        # branch coverage
        if runs.is_a?(Hash) && runs[:branches]
          total = covered = 0
          id = 0
          runs[:branches].each do |(_base_type, _, base_lineno), targets|
            i = 0
            targets.each do |(_target_type, _target_lineno), run|
              out << "BRDA:#{ base_lineno },#{ id },#{ i },#{ run }\n"
              total += 1
              covered += 1 if run > 0
              i += 1
            end
            id += 1
          end
          out << "BRF:#{ total }\n"
          out << "BRH:#{ covered }\n"
        end

        out << "end_of_record\n"
      end

      out
    end