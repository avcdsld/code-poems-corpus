def list_by_job_as_lazy(resource_group_name, automation_account_name, job_id, filter:nil, custom_headers:nil)
      response = list_by_job_async(resource_group_name, automation_account_name, job_id, filter:filter, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_by_job_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end