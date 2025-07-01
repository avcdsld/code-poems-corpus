def is_active?(page_name, product_types = nil)
      controller.controller_name.include?(page_name) || controller.action_name.include?(page_name) || (@product != nil && product_types !=nil && product_types.split(',').include?(@product.product_type) && !@product.name.include?('Historian'))
    end