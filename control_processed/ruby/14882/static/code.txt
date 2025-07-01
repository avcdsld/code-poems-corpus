def with_svg(doc)
      doc = Nokogiri::XML::Document.parse(
        doc.to_html(encoding: "UTF-8"), nil, "UTF-8"
      )
      svg = doc.at_css "svg"
      yield svg if svg && block_given?
      doc
    end