def to_depth new_depth
      return self if depth == new_depth

      color = Color.new :depth => new_depth
      if new_depth > self.depth
        %w'r g b a'.each do |part|
          color.send("#{part}=", (2**new_depth-1)/(2**depth-1)*self.send(part))
        end
      else
        # new_depth < self.depth
        %w'r g b a'.each do |part|
          color.send("#{part}=", self.send(part)>>(self.depth-new_depth))
        end
      end
      color
    end