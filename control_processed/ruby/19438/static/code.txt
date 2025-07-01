def conditional_assignment(variable, value, bool = true)
      variable.reference_amount += 1

      if current_scope.has_definition?(variable.type, variable.name) == bool
        variable.value = value

        current_scope.add_definition(variable)

        buffer_assignment_value(variable.value)
      end
    end