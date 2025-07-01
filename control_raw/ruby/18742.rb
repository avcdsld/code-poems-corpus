def index
      notifications = Correspondent::Notification.for_subscriber(params[:subscriber_type], params[:subscriber_id])
      render(json: notifications) if stale?(notifications)
    end