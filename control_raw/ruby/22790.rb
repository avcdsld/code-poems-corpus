def admin_index
      return if !user_is_allowed('redirects', 'view')            
      @domain = Domain.where(:domain => request.host_with_port).first      
      @redirects = @domain ? PermanentRedirect.where(:site_id => @domain.site_id).reorder(:priority).all : []            
      render :layout => 'caboose/admin'      
    end