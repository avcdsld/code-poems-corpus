def [](loader_name)
    loader = @loaders_by_name[loader_name]
    if loader.nil?
      # Unable to find the module private loader. Try resolving the module
      loader = private_loader_for_module(loader_name[0..-9]) if loader_name.end_with?(' private')
      raise Puppet::ParseError, _("Unable to find loader named '%{loader_name}'") % { loader_name: loader_name } if loader.nil?
    end
    loader
  end