def ariane
      if !Ariane.request_env || Ariane.request != request.object_id
        Ariane.request     = request.object_id
        Ariane.request_env = request.env
        Ariane.session     = session if Ariane.dynamic_breadcrumb
      end

      Ariane.breadcrumb
    end