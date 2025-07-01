def draw_form_group_fieldset(bootstrap, method)
      options = {}

      unless bootstrap.label[:hide]
        label_text = bootstrap.label[:text]
        label_text ||= ActionView::Helpers::Tags::Label::LabelBuilder
          .new(@template, @object_name.to_s, method, @object, nil).translation

        add_css_class!(options, "col-form-label pt-0")
        add_css_class!(options, bootstrap.label[:class])

        if bootstrap.horizontal?
          add_css_class!(options, bootstrap.label_col_class)
          add_css_class!(options, bootstrap.label_align_class)
        end

        label = content_tag(:legend, options) do
          label_text
        end
      end

      content_tag(:fieldset, class: "form-group") do
        content = "".html_safe
        content << label if label.present?
        content << draw_control_column(bootstrap, offset: bootstrap.label[:hide]) do
          yield
        end

        if bootstrap.horizontal?
          content_tag(:div, content, class: "row")
        else
          content
        end
      end
    end