def describe_layout(sobject_type, layout_id=nil)
      # Cache objects to avoid repeat lookups.
      @describe_layout_cache[sobject_type] ||={}

      # nil key is for full object.
      if @describe_layout_cache[sobject_type][layout_id].nil?
        response = call_soap_api(:describe_layout, :sObjectType => sobject_type, :recordTypeIds => layout_id)
        @describe_layout_cache[sobject_type][layout_id] = response
      else
        response = @describe_layout_cache[sobject_type][layout_id]
      end

      response
    end