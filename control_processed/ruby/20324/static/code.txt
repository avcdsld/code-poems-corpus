def save
      if @parse_object_id
        method = :put
        merge!(@op_fields) # use ops instead of our own view of the columns
      else
        method = :post
      end

      body = safe_hash.to_json
      data = @client.request(uri, method, body)

      if data
        # array ops can return mutated view of array which needs to be parsed
        object = Parse.parse_json(class_name, data)
        object = Parse.copy_client(@client, object)
        parse object
      end

      if @class_name == Parse::Protocol::CLASS_USER
        delete('password')
        delete(:username)
        delete(:password)
      end

      self
    end