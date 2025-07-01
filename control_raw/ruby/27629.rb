def update_name(service_id, snapshot_id, name)
      return unless service_id && snapshot_id && name
      verify_input_name(name)

      key = self.class.redis_key(service_id)
      # NOTE: idealy should watch on combination of (service_id, snapshot_id)
      # but current design doesn't support such fine-grained watching.
      client.watch(key)

      snapshot = client.hget(redis_key(service_id), snapshot_id)
      return nil unless snapshot
      snapshot = Yajl::Parser.parse(snapshot)
      snapshot["name"] = name

      res = client.multi do
        save_snapshot(service_id, snapshot)
      end

      unless res
        raise ServiceError.new(ServiceError::REDIS_CONCURRENT_UPDATE)
      end
      true
    end