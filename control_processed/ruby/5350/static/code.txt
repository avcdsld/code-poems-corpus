def insert(location, data)
      pages_to_add = nil
      if data.is_a? PDF
        @version = [@version, data.version].max
        pages_to_add = data.pages
        actual_value(@names ||= {}.dup).update data.names, &HASH_MERGE_NEW_NO_PAGE
        merge_outlines((@outlines ||= {}.dup), actual_value(data.outlines), location) unless actual_value(data.outlines).empty?
        if actual_value(@forms_data)
          actual_value(@forms_data).update actual_value(data.forms_data), &HASH_MERGE_NEW_NO_PAGE if data.forms_data
        else
          @forms_data = data.forms_data
        end
        warn 'Form data might be lost when combining PDF forms (possible conflicts).' unless data.forms_data.nil? || data.forms_data.empty?
      elsif data.is_a?(Array) && (data.select { |o| !(o.is_a?(Hash) && o[:Type] == :Page) }).empty?
        pages_to_add = data
      elsif data.is_a?(Hash) && data[:Type] == :Page
        pages_to_add = [data]
      else
        warn "Shouldn't add objects to the file unless they are PDF objects or PDF pages (an Array or a single PDF page)."
        return false # return false, which will also stop any chaining.
      end
      # pages_to_add.map! {|page| page.copy }
      catalog = rebuild_catalog
      pages_array = catalog[:Pages][:referenced_object][:Kids]
      page_count = pages_array.length
      if location < 0 && (page_count + location < 0)
        location = 0
      elsif location > 0 && (location > page_count)
        location = page_count
      end
      pages_array.insert location, pages_to_add
      pages_array.flatten!
      self
    end