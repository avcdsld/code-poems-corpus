def tags(name = nil)
      list = stable_sort_by(@tags + convert_ref_tags, &:tag_name)
      return list unless name
      list.select {|tag| tag.tag_name.to_s == name.to_s }
    end