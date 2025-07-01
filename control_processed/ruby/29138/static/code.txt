def tree_bank_string
      span = j_instance.getSpan
      text = j_instance.getText
      type = j_instance.getType
      res = ''
      start = span.getStart

      res << "(#{type} " if type != Java::opennlp.tools.parser.AbstractBottomUpParser::TOK_NODE

      j_instance.getChildren.each do |child|
        child_span = child.span
        res << text[start..child_span.getStart - 1] if start < child_span.getStart
        res << self.class.new(child).tree_bank_string
        start = child_span.getEnd
      end

      res << text[start..span.getEnd - 1] if start < span.getEnd
      res << ')' if type != Java::opennlp.tools.parser.AbstractBottomUpParser::TOK_NODE

      res
    end