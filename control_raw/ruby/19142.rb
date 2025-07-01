def facts_to_yaml(node = @node)
      # Add the header that Puppet needs to treat this as facts. Save the results
      # as a string in the option.
      f = facts(node)
      fact_file = f.to_yaml.split(/\n/)
      fact_file[0] = '--- !ruby/object:Puppet::Node::Facts' if fact_file[0] =~ /^---/
      fact_file.join("\n")
    end