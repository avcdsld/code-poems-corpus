def get_data_array(handles)
      return [] unless handles && handles.any?

      entity_class_name_for_soap_request = entity_class.name.split("::").last
      response = request(:get_data_array, "entityHandles" => {"#{entity_class_name_for_soap_request}Handle" => handles.collect(&:to_hash)})
      [response["#{entity_class.key}_data".intern]].flatten
    end