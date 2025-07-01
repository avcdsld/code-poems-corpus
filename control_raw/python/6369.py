def initialize_valid_actions(grammar: Grammar,
                             keywords_to_uppercase: List[str] = None) -> Dict[str, List[str]]:
    """
    We initialize the valid actions with the global actions. These include the
    valid actions that result from the grammar and also those that result from
    the tables provided. The keys represent the nonterminals in the grammar
    and the values are lists of the valid actions of that nonterminal.
    """
    valid_actions: Dict[str, Set[str]] = defaultdict(set)

    for key in grammar:
        rhs = grammar[key]

        # Sequence represents a series of expressions that match pieces of the text in order.
        # Eg. A -> B C
        if isinstance(rhs, Sequence):
            valid_actions[key].add(format_action(key, " ".join(rhs._unicode_members()), # pylint: disable=protected-access
                                                 keywords_to_uppercase=keywords_to_uppercase))

        # OneOf represents a series of expressions, one of which matches the text.
        # Eg. A -> B / C
        elif isinstance(rhs, OneOf):
            for option in rhs._unicode_members(): # pylint: disable=protected-access
                valid_actions[key].add(format_action(key, option,
                                                     keywords_to_uppercase=keywords_to_uppercase))

        # A string literal, eg. "A"
        elif isinstance(rhs, Literal):
            if rhs.literal != "":
                valid_actions[key].add(format_action(key, repr(rhs.literal),
                                                     keywords_to_uppercase=keywords_to_uppercase))
            else:
                valid_actions[key] = set()

    valid_action_strings = {key: sorted(value) for key, value in valid_actions.items()}
    return valid_action_strings