def record_from_current_or_find(klass, id, current)
      if current.is_a?(ActiveRecord::Base) && current.id.to_s == id
        # modifying the current object of a singular association
        current
      elsif current.respond_to?(:any?) && current.any? { |o| o.id.to_s == id }
        # modifying one of the current objects in a plural association
        current.detect { |o| o.id.to_s == id }
      else # attaching an existing but not-current object
        klass.find(id)
      end
    end