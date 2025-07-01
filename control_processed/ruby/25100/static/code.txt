def to_xml(parser)
      n = parser.new_node('date')
      n = parser.append_node(n, parser.new_text(CFDate::date_string(@value)))
      n
    end