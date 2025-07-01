def to_statement(self, parameter_values):
        """
        With the given values for each parameter, this method will return a policy statement that can be used
        directly with IAM.

        :param dict parameter_values: Dict containing values for each parameter defined in the template
        :return dict: Dictionary containing policy statement
        :raises InvalidParameterValues: If parameter values is not a valid dictionary or does not contain values
            for all parameters
        :raises InsufficientParameterValues: If the parameter values don't have values for all required parameters
        """

        missing = self.missing_parameter_values(parameter_values)
        if len(missing) > 0:
            # str() of elements of list to prevent any `u` prefix from being displayed in user-facing error message
            raise InsufficientParameterValues("Following required parameters of template '{}' don't have values: {}"
                                              .format(self.name, [str(m) for m in missing]))

        # Select only necessary parameter_values. this is to prevent malicious or accidental
        # injection of values for parameters not intended in the template. This is important because "Ref" resolution
        # will substitute any references for which a value is provided.
        necessary_parameter_values = {name: value for name, value in parameter_values.items()
                                      if name in self.parameters}

        # Only "Ref" is supported
        supported_intrinsics = {
            RefAction.intrinsic_name: RefAction()
        }

        resolver = IntrinsicsResolver(necessary_parameter_values, supported_intrinsics)
        definition_copy = copy.deepcopy(self.definition)

        return resolver.resolve_parameter_refs(definition_copy)