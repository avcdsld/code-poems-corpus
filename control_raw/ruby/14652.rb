def regular_error_handling?(ex) #:nodoc:
      if @error_block 
        return true if (ex.respond_to?(:exit_code) && ex.exit_code == 0)
        @error_block.call(ex)
      else
        true
      end
    end