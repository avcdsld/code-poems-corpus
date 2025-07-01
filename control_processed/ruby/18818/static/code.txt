def without(*args)
      args = args.flatten
      option(*args) do |options|
        options.store(
          :fields, args.inject(options[:fields] || {}){ |sub, field| sub.tap { sub[field] = 0 }}
        )
      end
    end