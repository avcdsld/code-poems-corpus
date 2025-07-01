def statistics_header(options)
      [
        { title: options[:title], width: :rest },
        { title: 'Hits',   align: :right, highlight: (options[:highlight] == :hits),   min_width: 4 },
        { title: 'Sum',    align: :right, highlight: (options[:highlight] == :sum),    min_width: 6 },
        { title: 'Mean',   align: :right, highlight: (options[:highlight] == :mean),   min_width: 6 },
        { title: 'StdDev', align: :right, highlight: (options[:highlight] == :stddev), min_width: 6 },
        { title: 'Min',    align: :right, highlight: (options[:highlight] == :min),    min_width: 6 },
        { title: 'Max',    align: :right, highlight: (options[:highlight] == :max),    min_width: 6 },
        { title: '95 %tile',    align: :right, highlight: (options[:highlight] == :percentile_interval),  min_width: 11 }
      ]
    end