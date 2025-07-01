def target_by_type(type)
      result = []
      @relationship.each do |cur_rels|
        result << cur_rels.target if cur_rels.type.include?(type)
      end
      result
    end