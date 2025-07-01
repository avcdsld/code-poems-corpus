def list_directory(dir_path, opts = {})
      url     = obj_url(dir_path)
      headers = gen_headers(opts)
      query_parameters = {}

      limit = opts[:limit] || MAX_LIMIT
      raise ArgumentError unless 0 < limit && limit <= MAX_LIMIT
      query_parameters[:limit] = limit

      marker = opts[:marker]
      if marker
        raise ArgumentError unless marker.is_a? String
        query_parameters[:marker] = marker
      end

      attempt(opts[:attempts]) do
        method = opts[:head] ? :head : :get
        result = @client.send(method, url, query_parameters, headers)
        raise unless result.is_a? HTTP::Message

        if result.status == 200
          raise unless result.headers['Content-Type'] ==
                       'application/x-json-stream; type=directory'

          return true, result.headers if method == :head

          json_chunks = result.body.split("\n")

          if json_chunks.size > limit
            raise CorruptResult
          end

          dir_entries = json_chunks.map { |i| JSON.parse(i) }

          return dir_entries, result.headers
        end

        raise_error(result)
      end
    end