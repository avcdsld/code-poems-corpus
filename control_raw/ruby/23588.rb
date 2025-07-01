def load_cookbooks(cookbook_names)
        Strainer.ui.debug "Sandbox#load_cookbooks(#{cookbook_names.inspect})"
        cookbook_names.collect{ |cookbook_name| load_cookbook(cookbook_name) }
      end