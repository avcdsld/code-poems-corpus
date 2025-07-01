def send_org_invite(user, invite)
      # Generate token if not generated
      user.send(:generate_confirmation_token!) if !user.confirmed? && user.confirmation_token.blank?

      MnoEnterprise::SystemNotificationMailer.organization_invite(invite).deliver_later

      # Update staged invite status
      invite.status = 'pending' if invite.status == 'staged'
      invite.notification_sent_at = Time.now unless invite.notification_sent_at.present?
      invite.save
    end