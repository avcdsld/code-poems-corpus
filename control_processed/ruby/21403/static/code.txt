def include_class?( writer_class )
      @writers.keys.each do | writer_instance |
        return true if writer_instance.is_a?( writer_class )
      end

      return false
    end