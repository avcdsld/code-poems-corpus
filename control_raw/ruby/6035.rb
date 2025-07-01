def check_for_status_code_failure(azure_response)
      fail MsRest::ValidationError, 'Azure response cannot be nil' if azure_response.nil?
      fail MsRest::ValidationError, 'Azure response cannot have empty response object' if azure_response.response.nil?
      fail MsRest::ValidationError, 'Azure response cannot have empty request object' if azure_response.request.nil?

      status_code = azure_response.response.status
      http_method = azure_response.request.method

      fail AzureOperationError, "Unexpected polling status code from long running operation #{status_code}" unless status_code === 200 || status_code === 202 ||
          (status_code === 201 && http_method === :put) ||
          (status_code === 204 && (http_method === :delete || http_method === :post))
    end