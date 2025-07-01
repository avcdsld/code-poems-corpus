def _get_json_table(console, address, parameters = {}, page_size = 500, records = nil, post = true)
      parameters['dir']        = 'DESC'
      parameters['startIndex'] = -1
      parameters['results']    = -1
      if post
        request = lambda { |p| AJAX.form_post(console, address, p) }
      else
        request = lambda { |p| AJAX.get(console, address.dup, AJAX::CONTENT_TYPE::JSON, p) }
      end

      response = request.call(parameters)
      data     = JSON.parse(response)
      # Don't attept to grab more records than there are.
      total = data['totalRecords']
      return [] if total.zero?
      total = records.nil? ? total : [records, total].min
      rows  = []
      parameters['results'] = page_size
      while rows.length < total
        parameters['startIndex'] = rows.length
        data = JSON.parse(request.call(parameters))
        rows.concat data['records']
      end
      rows
    end