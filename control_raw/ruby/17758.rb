def create
      return render json: { errors: { message: "#{container} not found" } }, status: :not_found unless dashboard.present?

      @widget = dashboard.widgets.create(widget_create_params)
      return render json: { errors: (widget && widget.errors).to_a }, status: :bad_request unless widget.present? && widget.valid?

      MnoEnterprise::EventLogger.info('widget_create', current_user.id, "#{container} Widget Creation", widget)
      @no_content = true
      render 'show'
    end