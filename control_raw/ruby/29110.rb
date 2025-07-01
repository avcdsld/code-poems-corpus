def add_parameterized_rules(field, rules)
      rules.each_pair do |key, params|
        add_single_rule(field, key, params)
      end
    end