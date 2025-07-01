def human_xor_01(X, y, model_generator, method_name):
    """ XOR (false/true)

    This tests how well a feature attribution method agrees with human intuition
    for an eXclusive OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough but not both: +6 points

    transform = "identity"
    sort_order = 4
    """
    return _human_xor(X, model_generator, method_name, False, True)