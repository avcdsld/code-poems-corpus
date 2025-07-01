def prune_tilt_templates!
      mapping = ::Tilt.default_mapping
      mapping.lazy_map.each_key do |key|
        begin
          mapping[key]
        rescue LoadError, NameError
        end
      end
      mapping.lazy_map.clear
    end