def build_records(amount, per_query, &block)
      amount.times do
        index = last_id_in_database + @records.size + 1
        record = Record.new(@model_class, index)
        @records << record
        block.call(record, index) if block
        save_records if @records.size >= per_query
      end
    end