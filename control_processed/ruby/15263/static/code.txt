def to_html(placeholder=random_canvas_id)
      chart_hash_must_be_present
      script = load_dependencies('web_frameworks')
      @div_id = placeholder
      script << high_chart_css(placeholder)
      # Helps to denote either of the three classes.
      chart_class = extract_chart_class
      # When user wants to plot a HighMap
      if chart_class == 'Map'
        script << high_map(placeholder, self)
      # When user wants to plot a HighStock
      elsif chart_class == 'StockChart'
        script << high_stock(placeholder, self)
      # When user wants to plot a HighChart
      elsif chart_class == 'Chart'
        script << high_chart(placeholder, self)
      end
      script
    end