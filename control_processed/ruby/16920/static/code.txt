def print_topics(words_per_topic = 10)
      raise 'No vocabulary loaded.' unless @vocab

      beta.each_with_index do |topic, topic_num|
        # Sort the topic array and return the sorted indices of the best scores
        indices = topic.zip((0...@vocab.size).to_a).sort { |x| x[0] }.map { |_i, j| j }.reverse[0...words_per_topic]

        puts "Topic #{topic_num}"
        puts "\t#{indices.map { |i| @vocab[i] }.join("\n\t")}"
        puts ''
      end

      nil
    end