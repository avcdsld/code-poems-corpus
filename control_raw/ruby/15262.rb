def draw_js_spreadsheet(data, element_id)
      js = ''
      js << "\n function #{chart_function_name(element_id)}() {"
      js << "\n   var query = new google.visualization.Query('#{data}');"
      js << "\n   query.send(#{query_response_function_name(element_id)});"
      js << "\n }"
      js << "\n function #{query_response_function_name(element_id)}(response) {"
      js << "\n   var data_table = response.getDataTable();"
      js << "\n   var table = new google.visualization.Table"\
            "(document.getElementById('#{element_id}'));"
      js << add_listeners_js('table')
      js << "\n 	table.draw(data_table, #{js_parameters(@options)});"
      js << "\n };"
      js
    end