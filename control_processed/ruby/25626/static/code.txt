def merge_attributes(attrs={})
    # copy attributes from the parent module fields array
    @attributes = self.class.attributes_from_module
    # populate the attributes with values from the attrs provided to init.
    @attributes.keys.each do |name|
      write_attribute name, attrs[name] if attrs[name]
    end
    # If this is an existing record, blank out the modified_attributes hash
    @modified_attributes = {} unless new?
  end