def render(name, view_context)
      hooks[name].map do |hook|
        hook.render(view_context)
      end.join("").html_safe
    end