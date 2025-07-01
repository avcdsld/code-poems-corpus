def clear_scroll( scroll_ids )
      response = delete "/_search/scroll", body: {scroll_id: Array(scroll_ids)}, action: "search.clear_scroll", rest_api: "clear_scroll"
      response.body
    end