def update_expiration_date(connection, new_date)
      xml = connection.make_xml('VulnerabilityExceptionUpdateExpirationDateRequest',
                                { 'exception-id' => @id,
                                  'expiration-date' => new_date })
      connection.execute(xml, '1.2').success
    end