def refresh_icon
      return nil unless @in_jss
      fresh_data = @api.get_rsrc(@rest_rsrc)[self.class::RSRC_OBJECT_KEY]
      subset_key = @self_service_data_config[:self_service_subset] ? @self_service_data_config[:self_service_subset] : :self_service

      ss_data = fresh_data[subset_key]

      icon_data = ss_data[:self_service_icon]
      @icon = JSS::Icon.new icon_data
    end