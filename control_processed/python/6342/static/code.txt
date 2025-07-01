def get_valid_actions(name_mapping: Dict[str, str],
                      type_signatures: Dict[str, Type],
                      basic_types: Set[Type],
                      multi_match_mapping: Dict[Type, List[Type]] = None,
                      valid_starting_types: Set[Type] = None,
                      num_nested_lambdas: int = 0) -> Dict[str, List[str]]:
    """
    Generates all the valid actions starting from each non-terminal. For terminals of a specific
    type, we simply add a production from the type to the terminal. For all terminal `functions`,
    we additionally add a rule that allows their return type to be generated from an application of
    the function.  For example, the function ``<e,<r,<d,r>>>``, which takes three arguments and
    returns an ``r`` would generate a the production rule ``r -> [<e,<r,<d,r>>>, e, r, d]``.

    For functions that do not contain ANY_TYPE or placeholder types, this is straight-forward.
    When there are ANY_TYPES or placeholders, we substitute the ANY_TYPE with all possible basic
    types, and then produce a similar rule.  For example, the identity function, with type
    ``<#1,#1>`` and basic types ``e`` and ``r``,  would produce the rules ``e -> [<#1,#1>, e]`` and
    ``r -> [<#1,#1>, r]``.

    We additionally add a valid action from the start symbol to all ``valid_starting_types``.

    Parameters
    ----------
    name_mapping : ``Dict[str, str]``
        The mapping of names that appear in your logical form languages to their aliases for NLTK.
        If you are getting all valid actions for a type declaration, this can be the
        ``COMMON_NAME_MAPPING``.
    type_signatures : ``Dict[str, Type]``
        The mapping from name aliases to their types. If you are getting all valid actions for a
        type declaration, this can be the ``COMMON_TYPE_SIGNATURE``.
    basic_types : ``Set[Type]``
        Set of all basic types in the type declaration.
    multi_match_mapping : ``Dict[Type, List[Type]]`` (optional)
        A mapping from `MultiMatchNamedBasicTypes` to the types they can match. This may be
        different from the type's ``types_to_match`` field based on the context. While building action
        sequences that lead to complex types with ``MultiMatchNamedBasicTypes``, if a type does not
        occur in this mapping, the default set of ``types_to_match`` for that type will be used.
    valid_starting_types : ``Set[Type]``, optional
        These are the valid starting types for your grammar; e.g., what types are we allowed to
        parse expressions into?  We will add a "START -> TYPE" rule for each of these types.  If
        this is ``None``, we default to using ``basic_types``.
    num_nested_lambdas : ``int`` (optional)
        Does the language used permit lambda expressions?  And if so, how many nested lambdas do we
        need to worry about?  We'll add rules like "<r,d> -> ['lambda x', d]" for all complex
        types, where the variable is determined by the number of nestings.  We currently only
        permit up to three levels of nesting, just for ease of implementation.
    """
    valid_actions: Dict[str, Set[str]] = defaultdict(set)

    valid_starting_types = valid_starting_types or basic_types
    for type_ in valid_starting_types:
        valid_actions[str(START_TYPE)].add(_make_production_string(START_TYPE, type_))

    complex_types = set()
    for name, alias in name_mapping.items():
        # Lambda functions and variables associated with them get produced in specific contexts. So
        # we do not add them to ``valid_actions`` here, and let ``GrammarState`` deal with it.
        # ``var`` is a special function that some languages (like LambdaDCS) use within lambda
        # functions to indicate the use of a variable (eg.: ``(lambda x (fb:row.row.year (var x)))``)
        # We do not have to produce this function outside the scope of lambda. Even within lambdas,
        # it is a lot easier to not do it, and let the action sequence to logical form transformation
        # logic add it to the output logical forms instead.
        if name in ["lambda", "var", "x", "y", "z"]:
            continue
        name_type = type_signatures[alias]
        # Type to terminal productions.
        for substituted_type in substitute_any_type(name_type, basic_types):
            valid_actions[str(substituted_type)].add(_make_production_string(substituted_type, name))
        # Keeping track of complex types.
        if isinstance(name_type, ComplexType) and name_type != ANY_TYPE:
            complex_types.add(name_type)

    for complex_type in complex_types:
        for substituted_type in substitute_any_type(complex_type, basic_types):
            for head, production in _get_complex_type_production(substituted_type,
                                                                 multi_match_mapping or {}):
                valid_actions[str(head)].add(production)

    # We can produce complex types with a lambda expression, though we'll leave out
    # placeholder types for now.
    for i in range(num_nested_lambdas):
        lambda_var = chr(ord('x') + i)
        # We'll only allow lambdas to be functions that take and return basic types as their
        # arguments, for now.  Also, we're doing this for all possible complex types where
        # the first and second types are basic types. So we may be overgenerating a bit.
        for first_type in basic_types:
            for second_type in basic_types:
                key = ComplexType(first_type, second_type)
                production_string = _make_production_string(key, ['lambda ' + lambda_var, second_type])
                valid_actions[str(key)].add(production_string)

    valid_action_strings = {key: sorted(value) for key, value in valid_actions.items()}
    return valid_action_strings