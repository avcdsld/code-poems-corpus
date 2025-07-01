def dispatch_to_controller(params, request)
      namespace = params[:component] || 'main'

      controller_name = params[:controller] + '_controller'
      action = params[:action]

      namespace_module = Object.const_get(namespace.camelize.to_sym)
      klass = namespace_module.const_get(controller_name.camelize.to_sym)
      controller = klass.new(@volt_app, params, request)

      # Use the 'meta' thread local to set the user_id for Volt.current_user
      meta_data = {}
      user_id = request.cookies['user_id']
      meta_data['user_id'] = user_id if user_id
      Thread.current['meta'] = meta_data

      controller.perform(action)
    end