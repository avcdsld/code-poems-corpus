def after_lazy(value)
      if lazy?(value)
        GraphQL::Execution::Lazy.new do
          result = sync_lazy(value)
          # The returned result might also be lazy, so check it, too
          after_lazy(result) do |final_result|
            yield(final_result) if block_given?
          end
        end
      else
        yield(value) if block_given?
      end
    end