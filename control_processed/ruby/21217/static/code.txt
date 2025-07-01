def generate_terminals(grammar)
      terminals = [:$EOF]

      grammar.terminals.each do |term|
        terminals << term.name.to_sym
      end

      return terminals
    end