def element_parents_recursive(sequence)
      parents = Array.new
      sequence.items.each do |i|
        parents << i if i.elements?
        i.sequences.each do |s|
          parents += element_parents_recursive(s)
        end
      end
      parents
    end