def query(params, base_return = [])
      params[:action] = 'query'
      params[:continue] = ''

      loop do
        result = post(params)
        yield(base_return, result['query']) if result.key?('query')
        break unless @use_continuation
        break unless result.key?('continue')
        continue = result['continue']
        continue.each do |key, val|
          params[key.to_sym] = val
        end
      end

      base_return
    end