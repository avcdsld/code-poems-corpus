def update_attribute(name, value)
      name = name.to_s
      verify_readonly_attribute(name)
      public_send("#{name}=", value)

      save(validate: false)
    end