def to_str(opts={})
      doc = REXML::Document.new
      @doc = doc

      doc.context[:attribute_quote] = :quote

      doc.add_element 'plist', {'version' => '1.0'}
      doc.root << opts[:root].to_xml(self)

      formatter = if opts[:formatted] then
        f = REXML::Formatters::Pretty.new(2)
        f.compact = true
        f.width = Float::INFINITY
        f
      else
        REXML::Formatters::Default.new
      end

      str = formatter.write(doc.root, "")
      str1 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n" + str + "\n"
      str1.force_encoding('UTF-8') if str1.respond_to?(:force_encoding)

      return str1
    end