def remove(id, resource_ids)
      params = {
        id: id,
        resource_ids: resource_ids
      }
      requires params
      DataSift.request(:PUT, 'source/resource/remove', @config, params)
    end