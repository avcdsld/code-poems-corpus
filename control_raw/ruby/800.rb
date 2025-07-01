def slice(index, num)
      ensure_unpacked!
      MultiEventStream.new(@unpacked_times.slice(index, num), @unpacked_records.slice(index, num))
    end