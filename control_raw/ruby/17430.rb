def inspect
      if INSPECT_FORMS.has_key? @node_type
        name, *params = INSPECT_FORMS[@node_type]

        params = params.map do |p|
          if p == :children
            children_inspect
          else
            send(p).inspect
          end
        end
        params << @al.inspect if @al && !@al.empty?
      else
        name = 'el'
        params = [self.node_type.inspect, children_inspect]
        params << @meta_priv.inspect unless @meta_priv.empty? && self.al.empty?
        params << self.al.inspect unless self.al.empty?
      end

      "md_#{name}(#{params.join(', ')})"
    end