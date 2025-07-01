def do_not_expect_views(*queries)
      if queries.nil? || queries.any?(&:nil?)
        raise ArgumentError, 'Query cannot be nil'
      end

      if queries.map{|query| view_exists?(query)}.any?
        raise ViewFoundError,
              "Some views matched #{Wait.parse_query_list(queries)}"
      end

      true
    end