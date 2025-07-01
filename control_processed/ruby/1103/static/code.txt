def all_functions
      classes.map do |klass|
        tasks = klass.tasks.select { |t| t.lang == :ruby } # only prewarm ruby functions
        tasks.map do |task|
          meth = task.meth
          underscored = klass.to_s.underscore.gsub('/','-')
          "#{underscored}-#{meth}" # function_name
        end
      end.flatten.uniq.compact
    end