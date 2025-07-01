def if_page(page_class, params={:using_params => {}},&block)
      page_class = class_from_string(page_class) if page_class.is_a? String
      return @current_page unless @current_page.class == page_class
      on_page(page_class, params, false, &block)
    end