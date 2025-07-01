def javascript(value = nil, attributes = {})
      if value.is_a?(Hash)
        attributes = value
        value      = nil
      elsif block_given? && value
        raise ArgumentError, "You can't pass both a block and a value to javascript -- please choose one."
      end

      script(attributes.merge(:type => "text/javascript")) do
        # Shouldn't this be a "cdata" HtmlPart?
        # (maybe, but the syntax is specific to javascript; it isn't
        # really a generic XML CDATA section.  Specifically,
        # ]]> within value is not treated as ending the
        # CDATA section by Firefox2 when parsing text/html,
        # although I guess we could refuse to generate ]]>
        # there, for the benefit of XML/XHTML parsers).
        output << raw("\n// <![CDATA[\n")
        if block_given?
          yield
        else
          output << raw(value)
        end
        output << raw("\n// ]]>")
        output.append_newline # this forces a newline even if we're not in pretty mode
      end

      output << raw("\n")
    end