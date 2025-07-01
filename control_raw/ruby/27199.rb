def loaded_headers
      explore = lambda do |obj|
        return obj if obj.is_a?(::ELFTools::Structs::ELFStruct)
        return obj.map(&explore) if obj.is_a?(Array)

        obj.instance_variables.map do |s|
          explore.call(obj.instance_variable_get(s))
        end
      end
      explore.call(self).flatten
    end