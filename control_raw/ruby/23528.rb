def target_summary(target_id)
      date_timestamp = Time.now.httpdate
      target_id_url = SUMMARY_URL + '/' + target_id
      target_id_suburl = '/summary' + '/' + target_id
      signature = self.build_signature(target_id_suburl, nil, 'GET', date_timestamp)
      authorization_header = "VWS " + @accesskey + ":" + signature
      begin
        RestClient.get(target_id_url, :'Date' => date_timestamp,
                                      :'Authorization' => authorization_header)
      rescue => e
        e.response
      end
    end