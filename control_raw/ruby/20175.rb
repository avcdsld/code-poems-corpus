def report_unused_steps
      # Remove any unused_steps that were in common modules and used
      # in another feature
      used_steps.each { |location| unused_steps.delete location }
      unused_steps.each do |location, name|
        puts "\n" + "Unused step: #{location} ".colorize(:yellow) +
             "'#{name}'".colorize(:light_yellow)
      end
    end