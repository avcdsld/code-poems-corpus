def update_iap!(app_id: nil, purchase_id: nil, data: nil)
      with_tunes_retry do
        r = request(:put) do |req|
          req.url("ra/apps/#{app_id}/iaps/#{purchase_id}")
          req.body = data.to_json
          req.headers['Content-Type'] = 'application/json'
        end
        handle_itc_response(r.body)
      end
    end