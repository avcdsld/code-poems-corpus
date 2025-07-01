def slice(*keys, **options)
      return super if options.include?(:raw)
      new_expires = expires_at(options, nil)
      options = Utils.without(options, :expires)

      with_updates(options) do |updates|
        @adapter.slice(*keys, **options).map do |key, entry|
          entry = invalidate_entry(key, entry, new_expires) do |new_entry|
            updates[key] = new_entry
          end
          next if entry.nil?
          value, _ = entry
          [key, value]
        end.reject(&:nil?)
      end
    end