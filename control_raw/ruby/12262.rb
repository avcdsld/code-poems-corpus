def to_html(threshold=30)
      table_thead = to_html_thead
      table_tbody = to_html_tbody(threshold)
      path = if index.is_a?(MultiIndex)
               File.expand_path('../iruby/templates/dataframe_mi.html.erb', __FILE__)
             else
               File.expand_path('../iruby/templates/dataframe.html.erb', __FILE__)
             end
      ERB.new(File.read(path).strip).result(binding)
    end