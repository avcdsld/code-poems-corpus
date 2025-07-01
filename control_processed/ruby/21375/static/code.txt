def document
      if @document.is_a?(URI)
        # Attempt to read page. May raise HTTPError.
        options = {}
        READER_OPTIONS.each { |key| options[key] = option(key) }
        request(@document, options)
      end
      if @document.is_a?(String)
        # Parse the page. May raise HTMLParseError.
        parsed = Reader.parse_page(@document, @page_info.encoding,
                                   option(:parser_options), option(:parser))
        @document = parsed.document
        @page_info.encoding = parsed.encoding
      end
      return @document if @document.is_a?(HTML::Node)
      raise RuntimeError, "No document to process"
    end