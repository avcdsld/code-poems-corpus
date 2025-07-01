def transform_response(response, options = {})
      # Now unpack the response into the data types.
      inner = response.delete("response")
      objects = unpack inner, options
      # Unpack pagination as a special case.
      if response.has_key?("pagination")
        paginated_response objects, response
      else
        objects
      end
    end