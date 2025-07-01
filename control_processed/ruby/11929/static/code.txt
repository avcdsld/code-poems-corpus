def render_partial_index(target, params)
        index_path = params.delete(:partial)
        partial    = partial_index_path(target, index_path, params[:partial_root])
        layout     = layout_path(params.delete(:layout), params[:layout_root])
        locals     = (params[:locals] || {}).merge(target: target, parameters: params)
        begin
          render params.merge(partial: partial, layout: layout, locals: locals)
        rescue ActionView::MissingTemplate
          partial = partial_index_path(target, index_path, 'activity_notification/notifications/default')
          render params.merge(partial: partial, layout: layout, locals: locals)
        end
      end