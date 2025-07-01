def each
      @model.transaction do
        begin
          declare_cursor
          if @join_dependency
            rows = Array.new
            last_id = nil

            while row = fetch_forward
              instantiated_row = @join_dependency.instantiate([row], @join_dependency.aliases).first

              current_id = instantiated_row[@join_dependency.join_root.primary_key]
              last_id ||= current_id
              if last_id == current_id
                rows << row
                last_id = current_id
              else
                yield @join_dependency.instantiate(rows, @join_dependency.aliases).first
                rows = [ row ]
              end
              last_id = current_id
            end

            if !rows.empty?
              yield @join_dependency.instantiate(rows, @join_dependency.aliases).first
            end
          else
            while row = fetch_forward
              yield @model.instantiate(row)
            end
          end
        ensure
          close_cursor
        end
      end
      nil
    end