def create_operation(fragment, filename = nil, lineno = nil)
      unless fragment.is_a?(GraphQL::Client::FragmentDefinition)
        raise TypeError, "expected fragment to be a GraphQL::Client::FragmentDefinition, but was #{fragment.class}"
      end

      if filename.nil? && lineno.nil?
        location = caller_locations(1, 1).first
        filename = location.path
        lineno = location.lineno
      end

      variables = GraphQL::Client::DefinitionVariables.operation_variables(self.schema, fragment.document, fragment.definition_name)
      type_name = fragment.definition_node.type.name

      if schema.query && type_name == schema.query.name
        operation_type = "query"
      elsif schema.mutation && type_name == schema.mutation.name
        operation_type = "mutation"
      elsif schema.subscription && type_name == schema.subscription.name
        operation_type = "subscription"
      else
        types = [schema.query, schema.mutation, schema.subscription].compact
        raise Error, "Fragment must be defined on #{types.map(&:name).join(", ")}"
      end

      doc_ast = GraphQL::Language::Nodes::Document.new(definitions: [
        GraphQL::Language::Nodes::OperationDefinition.new(
          operation_type: operation_type,
          variables: variables,
          selections: [
            GraphQL::Language::Nodes::FragmentSpread.new(name: fragment.name)
          ]
        )
      ])
      parse(doc_ast.to_query_string, filename, lineno)
    end