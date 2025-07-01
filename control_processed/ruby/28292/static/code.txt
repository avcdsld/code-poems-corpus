def set_value val, key=""
      oldval = @value
      if @klass == 'String'
        @value = val
      elsif @klass == 'Hash'
        #$log.debug " Variable setting hash #{key} to #{val}"
        oldval = @value[key]
        @value[key]=val
      elsif @klass == 'Array'
        #$log.debug " Variable setting array #{key} to #{val}"
        oldval = @value[key]
        @value[key]=val
      else
        oldval = @value
        @value = val
      end
      return if @update_command.nil?
      @update_command.each_with_index do |comm, ix|
        comm.call(self, *@args[ix]) unless comm.nil?
      end
      @dependents.each {|d| d.fire_property_change(d, oldval, val) } unless @dependents.nil?
    end