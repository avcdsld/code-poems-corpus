def op_type(params = {})
      if es_version_5_x? && (params.key?(:_op_type) || params.key?("_op_type"))
        params[:op_type] = params.delete(:_op_type)
      end
      params
    end