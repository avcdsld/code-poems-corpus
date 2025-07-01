def async_hypervisors_update
      task = Katello::Resources::Candlepin::Consumer.async_hypervisors(params[:owner], request.raw_post)
      async_task(::Actions::Katello::Host::Hypervisors, nil, :task_id => task['id'])

      render :json => task
    end