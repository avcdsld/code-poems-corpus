def inspect
      opts = options.reject { |k| %i[type name].include?(k) }
      meta_and_opts = meta.merge(opts).map { |k, v| "#{k}=#{v.inspect}" }
      %(#<#{self.class}[#{type.name}] name=#{name.inspect} #{meta_and_opts.join(' ')}>)
    end