def async_fetch_in_batch(handles, batch_size = 1000, &block)
      raise "No block given for the batch fetch request!" unless block_given?
      # Can't get data from an unfinished query
      unless async_is_complete?(handles)
        raise "Can't perform fetch on a query in state: #{async_state(handles)}"
      end

      # Now let's iterate over the results
      loop do
        rows = fetch_rows(prepare_operation_handle(handles), :next, batch_size)
        break if rows.empty?
        yield rows
      end
    end