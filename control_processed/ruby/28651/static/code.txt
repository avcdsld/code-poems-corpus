def get_widget_documents(widget_id, version_id=nil, participant_email=nil)
      Echochamber::Request.get_widget_documents(token, widget_id, version_id, participant_email)
    end