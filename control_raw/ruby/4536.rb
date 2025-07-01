def batch_requests(pipeline_params, limit = nil)
      limit ||= Process.respond_to?(:getrlimit) ? Process.getrlimit(:NOFILE).first : 256
      responses = []

      pipeline_params.each_slice(limit) do |params|
        responses.concat(requests(params))
      end

      responses
    end