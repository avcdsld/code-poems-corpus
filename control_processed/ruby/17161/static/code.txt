def create
      @object = resource.new(object_params)
      authorize_for(action: :create,
                    resource: resource.name.underscore.to_sym,
                    object: @object)
      if @object.save
        render json: @object.to_json, status: :created
      else
        render json: @object.errors, status: :unprocessable_entity
      end
    end