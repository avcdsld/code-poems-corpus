def run_job_flow(job_flow_config)
      params = {
        :operation => 'RunJobFlow',
      }.merge!(job_flow_config)
      aws_result = @aws_request.submit(params)
      yield aws_result if block_given?
      JSON.parse(aws_result)['JobFlowId']
    end