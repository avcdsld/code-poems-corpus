def notification(notifier, opts = {})
      Guard.state.session.guardfile_notification = { notifier.to_sym => opts }
    end