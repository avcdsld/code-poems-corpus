def plugin_info_by_id(plugin_id, opts={})
      found = all_plugins.find {|pe|
        pe.respond_to?(:plugin_id) && pe.plugin_id.to_s == plugin_id
      }
      if found
        get_monitor_info(found, opts)
      else
        nil
      end
    end