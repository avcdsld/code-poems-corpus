def train_project(project_id, training_type:nil, reserved_budget_in_hours:0, force_train:false, notification_email_address:nil, custom_headers:nil)
      response = train_project_async(project_id, training_type:training_type, reserved_budget_in_hours:reserved_budget_in_hours, force_train:force_train, notification_email_address:notification_email_address, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end