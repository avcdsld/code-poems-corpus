def save_contact(contact)
      request_xml = contact.to_xml

      response_xml = nil
      create_or_save = nil
      if contact.contact_id.nil? && contact.contact_number.nil?
        # Create new contact record.
        response_xml = http_put(@client, "#{@xero_url}/Contacts", request_xml, {})
        create_or_save = :create
      else
        # Update existing contact record.
        response_xml = http_post(@client, "#{@xero_url}/Contacts", request_xml, {})
        create_or_save = :save
      end

      response = parse_response(response_xml, {:request_xml => request_xml}, {:request_signature => "#{create_or_save == :create ? 'PUT' : 'POST'}/contact"})
      contact.contact_id = response.contact.contact_id if response.contact && response.contact.contact_id
      response
    end