def add_transition (self, input_symbol, state, action=None, next_state=None):

        '''This adds a transition that associates:

                (input_symbol, current_state) --> (action, next_state)

        The action may be set to None in which case the process() method will
        ignore the action and only set the next_state. The next_state may be
        set to None in which case the current state will be unchanged.

        You can also set transitions for a list of symbols by using
        add_transition_list(). '''

        if next_state is None:
            next_state = state
        self.state_transitions[(input_symbol, state)] = (action, next_state)