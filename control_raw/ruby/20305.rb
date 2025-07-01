def file_field(method, options = {})
      bootstrap = form_bootstrap.scoped(options.delete(:bootstrap))
      return super if bootstrap.disabled

      draw_form_group(bootstrap, method, options) do
        if bootstrap.custom_control
          content_tag(:div, class: "custom-file") do
            add_css_class!(options, "custom-file-input")
            remove_css_class!(options, "form-control")
            label_text = options.delete(:placeholder)
            concat super(method, options)

            label_options = { class: "custom-file-label" }
            label_options[:for] = options[:id] if options[:id].present?
            concat label(method, label_text, label_options)
          end
        else
          super(method, options)
        end
      end
    end