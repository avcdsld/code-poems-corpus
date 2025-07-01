def class_and_id(record_or_hash)
      if record_or_hash.is_a?(Hash)
        [record_or_hash[:class], record_or_hash[:id]]
      else
        [record_or_hash.class, Sunspot::Adapters::InstanceAdapter.adapt(record_or_hash).id]
      end
    end