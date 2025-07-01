def build_nested(object)
      this = self

      nested_object = Configuration.new
      children.each { |child| child.build(nested_object) }
      object.instance_exec { define_singleton_method(this.name) { nested_object } }

      object
    end