def match(class_name, term)
      the_class = JSS.api_object_class(class_name)
      raise JSS::UnsupportedError, "Class #{the_class} is not matchable" unless the_class.respond_to? :match
      the_class.match term, api: self
    end