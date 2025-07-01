def set_title(params)
    name, encoding = encode_utf16( params[:name], params[:name_encoding])

    formula = parse_series_formula(params[:name_formula])

    @title_name     = name
    @title_encoding = encoding
    @title_formula  = formula
  end