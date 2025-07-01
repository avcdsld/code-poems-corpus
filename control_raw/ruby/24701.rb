def unmarshall(signature, len = nil)
      if !len.nil?
        if @buffy.bytesize < @idx + len
          raise IncompleteBufferException
        end
      end
      sigtree = Type::Parser.new(signature).parse
      ret = []
      sigtree.each do |elem|
        ret << do_parse(elem)
      end
      ret
    end