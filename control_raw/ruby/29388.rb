def to_xml
      self.class.name == "TripIt::TpDateTime" ? xmlstr = "<DateTime>" : xmlstr = "<#{self.class.name.split("::").last}>"
      self.respond_to?("sequence") ? arr = self.sequence : arr = self.instance_variables
      arr.each do |key|
        next if key == "@client" # Skip the OAuth client
        value = self.instance_variable_get(key)
        next if value.nil?
        if value.is_a?(Array)
          next if value.empty?
          # We have an array of objects. First get the type of class
          objectType = value.first.class.name.split("::").last
          # Now get all of the objects' to_xml values    
          xmlArr = value.map { |mem| mem.to_xml }
          xmlstr << "<#{camelize(key[1..-1])}>#{xmlArr}</#{camelize(key[1..-1])}>"
        elsif value.class.name.split("::").first == "TripIt"
          # If it's a single one of our objects, call its to_xml method
          xmlstr << value.to_xml
        elsif key=~/date_/
          xmlstr << TripIt::TpDateTime.new(value).to_xml
        else
          xmlstr << "<#{key[1..-1]}>#{value}</#{key[1..-1]}>"
        end
      end
      self.class.name == "TripIt::TpDateTime" ? xmlstr << "</DateTime>" : xmlstr << "</#{self.class.name.split("::").last}>"
    end