def show(options = {}, &block)
      current_authorizer.authorize :show, resource
      respond_with resource, options, &block
    end