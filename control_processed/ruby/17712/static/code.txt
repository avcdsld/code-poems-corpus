def parse(node)
      node.xpath('*').each do |node_child|
        case node_child.name
        when 'stSnd'
          @start_sound = Sound.new(parent: self).parse(node_child.xpath('p:snd').first) unless node_child.xpath('p:snd').first.nil?
        when 'endSnd'
          @end_sound = Sound.new(parent: self).parse(node_child.xpath('p:snd').first) unless node_child.xpath('p:snd').first.nil?
        end
      end
      self
    end