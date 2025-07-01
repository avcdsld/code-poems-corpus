def create
      @dashboard_template = MnoEnterprise::Impac::Dashboard.new(dashboard_template_params.merge(dashboard_type: 'template'))

      # Abort on failure
      unless @dashboard_template.save
        return render json: { errors: dashboard_template.errors }, status: :bad_request
      end
        
      MnoEnterprise::EventLogger.info('dashboard_template_create', current_user.id, 'Dashboard Template Creation', dashboard_template)
      render 'show'
    end