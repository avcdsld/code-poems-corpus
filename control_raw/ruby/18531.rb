def reorder_buffers(index_buffer, index_map, vertex_count)
      # Create a copy of all attributes for reordering
      sorted_attributes = {}
      @attributes.each do |key, attribute|
        next if key == :index
        source_array = attribute.array
        sorted_attributes[key] = source_array.class.new(attribute.item_size * vertex_count)
      end

      # move attribute positions based on the new index map
      vertex_count.times do |new_vid|
        vid = index_map[new_vid]
        @attributes.each do |key, attribute|
          next if key == :index
          attr_array = attribute.array
          attr_size = attribute.item_size
          sorted_attr = sorted_attributes[key]
          attr_size.times do |k|
            sorted_attr[new_vid * attr_size + k] = attr_array[vid * attr_size + k]
          end
        end
      end

      # Carry the new sorted buffers locally
      @attributes[:index].array = index_buffer
      @attributes.each do |key, attribute|
        next if key == :index
        attribute.array = sorted_attributes[key]
        attribute.num_items = attribute.item_size * vertex_count
      end
    end