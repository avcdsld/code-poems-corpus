def update(record)
      result = self.class.put(worksheet_url + "/" + record.id,
        :body => { "fields" => record.fields_for_update }.to_json,
        :headers => { "Content-type" => "application/json" }).parsed_response

      check_and_raise_error(result)

      record.override_attributes!(result_attributes(result))
      record

    end