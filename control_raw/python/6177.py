def _execute_expression(self, expression: Any):
        """
        This does the bulk of the work of executing a logical form, recursively executing a single
        expression.  Basically, if the expression is a function we know about, we evaluate its
        arguments then call the function.  If it's a list, we evaluate all elements of the list.
        If it's a constant (or a zero-argument function), we evaluate the constant.
        """
        # pylint: disable=too-many-return-statements
        if isinstance(expression, list):
            if isinstance(expression[0], list):
                function = self._execute_expression(expression[0])
            elif expression[0] in self._functions:
                function = self._functions[expression[0]]
            else:
                if isinstance(expression[0], str):
                    raise ExecutionError(f"Unrecognized function: {expression[0]}")
                else:
                    raise ExecutionError(f"Unsupported expression type: {expression}")
            arguments = [self._execute_expression(arg) for arg in expression[1:]]
            try:
                return function(*arguments)
            except (TypeError, ValueError):
                traceback.print_exc()
                raise ExecutionError(f"Error executing expression {expression} (see stderr for stack trace)")
        elif isinstance(expression, str):
            if expression not in self._functions:
                raise ExecutionError(f"Unrecognized constant: {expression}")
            # This is a bit of a quirk in how we represent constants and zero-argument functions.
            # For consistency, constants are wrapped in a zero-argument lambda.  So both constants
            # and zero-argument functions are callable in `self._functions`, and are `BasicTypes`
            # in `self._function_types`.  For these, we want to return
            # `self._functions[expression]()` _calling_ the zero-argument function.  If we get a
            # `FunctionType` in here, that means we're referring to the function as a first-class
            # object, instead of calling it (maybe as an argument to a higher-order function).  In
            # that case, we return the function _without_ calling it.
            # Also, we just check the first function type here, because we assume you haven't
            # registered the same function with both a constant type and a `FunctionType`.
            if isinstance(self._function_types[expression][0], FunctionType):
                return self._functions[expression]
            else:
                return self._functions[expression]()
            return self._functions[expression]
        else:
            raise ExecutionError("Not sure how you got here. Please open a github issue with details.")