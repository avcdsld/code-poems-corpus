def set_x_axis(params)
    name, encoding = encode_utf16(params[:name], params[:name_encoding])
    formula = parse_series_formula(params[:name_formula])

    @x_axis_name     = name
    @x_axis_encoding = encoding
    @x_axis_formula  = formula
  end