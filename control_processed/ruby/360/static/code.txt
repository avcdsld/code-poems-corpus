def documents
      @documents ||= collections.reduce(Set.new) do |docs, (_, collection)|
        docs + collection.docs + collection.files
      end.to_a
    end