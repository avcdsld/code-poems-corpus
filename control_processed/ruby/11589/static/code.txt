def deliver!
      ::Notification.create!(
        :audience => Notification::AUDIENCE_USER,
        :notification_blueprint => blueprint,
        :initiator => initiator,
        :message => message,
        :subject => subject,
        :actions => {
          :links => links
        }
      )
    end