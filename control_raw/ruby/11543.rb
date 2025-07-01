def condition_from_association_constraint(association, value)
      # when the reverse association is a :belongs_to, the id for the associated object only exists as
      # the primary_key on the other table. so for :has_one and :has_many (when the reverse is :belongs_to),
      # we have to use the other model's primary_key.
      #
      # please see the relevant tests for concrete examples.

      field =
        if association.belongs_to?
          association.foreign_key
        else
          association.klass.primary_key
        end

      table = association.belongs_to? ? active_scaffold_config.model.table_name : association.table_name
      value = association.klass.find(value).send(association.primary_key) if association.primary_key

      if association.polymorphic?
        unless value.is_a?(Array) && value.size == 2
          raise ActiveScaffold::MalformedConstraint, polymorphic_constraint_error(association), caller
        end
        condition = {table => {association.foreign_type => value[0], field => value[1]}}
      else
        condition = {table => {field.to_s => value}}
      end

      condition
    end