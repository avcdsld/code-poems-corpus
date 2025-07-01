def reformat_timeseries data, as_datetime = false, include_unit = false
      data.map do |d|
        time = (as_datetime) ? DateTime.parse(d['ts']) : DateTime.parse(d['ts']).to_i
        val = HaystackRuby::Object.new(d['val'])
        r = {:time => time, :value => val.value}
        r[:unit] = val.unit if include_unit
        r
      end
    end