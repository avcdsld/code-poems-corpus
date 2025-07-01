def remove_from_index(name, key)
      index(name).delete(key)
      index(:"#{name}_to_s").delete(key.to_s)
      index(:"#{name}_to_sym").delete(:"#{key}") if to_sym?(key)
    end