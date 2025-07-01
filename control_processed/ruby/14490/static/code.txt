def type
            name = (self.class.name or self.class.superclass.name or self.native_type.name)

            name.split("::").last.to_sym
        end