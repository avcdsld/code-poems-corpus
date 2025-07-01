def build_tasks
      all_output.split("\n").map do |task|
        next unless task.start_with? "rake"
        task.split("#").map { |t| t.strip.sub(/^rake /, "") }
      end.compact
    end