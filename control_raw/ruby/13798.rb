def process_chain(data, filter_chain)
      # First we extract the data through the chain...
      filter_chain.each do |filter|
        data = filter.extract(data)
      end

      # Then we process the data through the chain *backwards*
      filter_chain.reverse.each do |filter|
        data = filter.process(data)
      end

      # Finally, a little bit of cleanup, just because
      data.gsub!(/<p><\/p>/) do
        ''
      end

      data
    end