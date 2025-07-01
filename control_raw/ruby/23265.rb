def create_job_candidate(candidate, shortcode, stage_slug = nil)
      shortcode = "#{shortcode}/#{stage_slug}" if stage_slug

      response = post_request("jobs/#{shortcode}/candidates") do |request|
        request.body = @transform_from.apply(:candidate, candidate).to_json
      end

      @transform_to.apply(:candidate, response['candidate'])
    end