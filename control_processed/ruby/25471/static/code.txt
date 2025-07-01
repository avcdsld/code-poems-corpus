def basic_publish(payload, xchg, routing_key, opts = {})
      xchg = xchg_find_or_create(xchg) unless xchg.respond_to? :name

      xchg.publish payload, opts.merge(routing_key: routing_key)

      self
    end