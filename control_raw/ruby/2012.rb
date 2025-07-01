def ensure_hook_type_sections_exist(hash)
      Overcommit::Utils.supported_hook_type_classes.each do |hook_type|
        hash[hook_type] ||= {}
        hash[hook_type]['ALL'] ||= {}
      end
    end