def unregister_exporter(mime_types, exporter = nil)
      unless mime_types.is_a? Array
        if mime_types.is_a? String
          mime_types = [mime_types]
        else # called with no mime type
          exporter = mime_types
          mime_types = nil
        end
      end

      self.config = hash_reassoc(config, :exporters) do |_exporters|
        _exporters.each do |mime_type, exporters_array|
          next if mime_types && !mime_types.include?(mime_type)
          if exporters_array.include? exporter
            _exporters[mime_type] = exporters_array.dup.delete exporter
          end
        end
      end
    end