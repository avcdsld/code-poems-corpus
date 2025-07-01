def take_while(&predicate)
      filter("take_while") do |yielder, all_done|
        each do |element|
          throw all_done unless yield(element)
          yielder.call(element)
        end
      end
    end