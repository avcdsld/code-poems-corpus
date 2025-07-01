def qualify_class_name(klass_name)
    unless @namespace.nil? || @namespace.blank? || klass_name.include?('::')
      namespaces = @namespace.split(/\.|::/)
      namespaces << klass_name
      klass_name = namespaces.join '::'
    end
    klass_name.camelize
  end