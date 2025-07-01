def add_from_catalog(catalog, test_module)
      coverable_resources = catalog.to_a.reject { |resource| !test_module.nil? && filter_resource?(resource, test_module) }
      coverable_resources.each do |resource|
        add(resource)
      end
    end