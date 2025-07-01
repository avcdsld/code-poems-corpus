def index
      @tag = params[:tag]
      set_vars
      set_paginator

      @meta = {}
      @meta[:title]     = "#{Blogo.config.site_title} - #{Blogo.config.site_subtitle}"
      @meta[:site_name] = Blogo.config.site_title
      @meta[:keywords]  = Blogo.config.keywords
      @meta[:type]      = 'website'
    end