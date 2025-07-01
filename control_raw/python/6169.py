def execute_action_sequence(self, action_sequence: List[str], side_arguments: List[Dict] = None):
        """
        Executes the program defined by an action sequence directly, without needing the overhead
        of translating to a logical form first.  For any given program, :func:`execute` and this
        function are equivalent, they just take different representations of the program, so you
        can use whichever is more efficient.

        Also, if you have state or side arguments associated with particular production rules
        (e.g., the decoder's attention on an input utterance when a predicate was predicted), you
        `must` use this function to execute the logical form, instead of :func:`execute`, so that
        we can match the side arguments with the right functions.
        """
        # We'll strip off the first action, because it doesn't matter for execution.
        first_action = action_sequence[0]
        left_side = first_action.split(' -> ')[0]
        if left_side != '@start@':
            raise ExecutionError('invalid action sequence')
        remaining_side_args = side_arguments[1:] if side_arguments else None
        return self._execute_sequence(action_sequence[1:], remaining_side_args)[0]