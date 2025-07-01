def template_finder(chef_run, cookbook_name)
      if Chef::Provider.const_defined?(:TemplateFinder) # Chef 11+
        Chef::Provider::TemplateFinder.new(chef_run.run_context, cookbook_name, chef_run.node)
      else
        nil
      end
    end