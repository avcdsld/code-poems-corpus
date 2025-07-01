def inspect
      ss = if @source.respond_to?(:join)
             @source.map(&:inspect).join(', ')
           elsif @source.is_a?(Proc)
             "?proc"
           else
             @source.inspect
           end

      ms = @metadata.reject { |_, v| v.nil? }
      ms.merge!(delta: delta) if delta != 1
      ms = ms.map { |k, v| "#{k}: #{v.inspect}" }.join(', ')

      "P[#{ss}#{", #{ms}" unless ms.empty?}]"
    end