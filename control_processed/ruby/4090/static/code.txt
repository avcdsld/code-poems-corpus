def awesome_ripple_document_instance(object)
      return object.inspect if !defined?(::ActiveSupport::OrderedHash)
      return awesome_object(object) if @options[:raw]
      exclude_assoc = @options[:exclude_assoc] or @options[:exclude_associations]

      data = object.attributes.inject(::ActiveSupport::OrderedHash.new) do |hash, (name, value)|
        hash[name.to_sym] = object.send(name)
        hash
      end

      unless exclude_assoc
        data = object.class.embedded_associations.inject(data) do |hash, assoc|
          hash[assoc.name] = object.get_proxy(assoc) # Should always be array or Ripple::EmbeddedDocument for embedded associations
          hash
        end
      end

      "#{object} " << awesome_hash(data)
    end