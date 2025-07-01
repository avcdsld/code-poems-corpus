def extract_literal_or_array_of_literals(s)
      literals = []
      braces_stack = []
      acc = []
      consume_literal = proc do
        acc_str = acc.join
        if acc_str =~ literal_re
          literals << strip_literal(acc_str)
          acc = []
        else
          return nil
        end
      end
      s.each_char.with_index do |c, i|
        if c == '['
          return nil unless braces_stack.empty?
          braces_stack.push(i)
        elsif c == ']'
          break
        elsif c == ','
          consume_literal.call
          break if braces_stack.empty?
        elsif c =~ VALID_KEY_CHARS || /['":]/ =~ c
          acc << c
        elsif c != ' '
          return nil
        end
      end
      consume_literal.call unless acc.empty?
      literals
    end