def copy(secure = false)
      # since only the Content streams are modified (Resource hashes are created anew),
      # it should be safe (and a lot faster) to create a deep copy only for the content hashes and streams.
      delete :Parent
      prep_content_array
      page_copy = clone
      page_copy[:Contents] = page_copy[:Contents].map do |obj|
        obj = obj.dup
        obj[:referenced_object] = obj[:referenced_object].dup if obj[:referenced_object]
        obj[:referenced_object][:raw_stream_content] = obj[:referenced_object][:raw_stream_content].dup if obj[:referenced_object] && obj[:referenced_object][:raw_stream_content]
        obj
      end
      if page_copy[:Resources]
        page_res = page_copy[:Resources] = page_copy[:Resources].dup
        page_res = page_copy[:Resources][:referenced_object] = page_copy[:Resources][:referenced_object].dup if page_copy[:Resources][:referenced_object]
        page_res.each do |k, v|
          v = page_res[k] = v.dup if v.is_a?(Array) || v.is_a?(Hash)
          v = v[:referenced_object] = v[:referenced_object].dup if v.is_a?(Hash) && v[:referenced_object]
        end
      end
      page_copy.instance_exec(secure || @secure_injection) { |s| secure_for_copy if s; init_contents; self }
    end