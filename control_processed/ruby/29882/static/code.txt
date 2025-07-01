def link_to_tracked_unless_current(name, track_path = "/", options = {}, html_options = {}, &block)
      raise AnalyticsError.new("You must set Rubaidh::GoogleAnalytics.defer_load = false to use outbound link tracking") if GoogleAnalytics.defer_load == true
      html_options.merge!({:onclick =>tracking_call(track_path)})
      link_to_unless current_page?(options), name, options, html_options, &block
    end