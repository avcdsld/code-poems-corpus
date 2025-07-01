def find_related(doc, max_nearest = 3, &block)
      carry =
        proximity_array_for_content(doc, &block).reject { |pair| pair[0].eql? doc }
      result = carry.collect { |x| x[0] }
      result[0..max_nearest - 1]
    end