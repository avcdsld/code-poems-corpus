def assoc(inst, **changes):
    """
    Copy *inst* and apply *changes*.

    :param inst: Instance of a class with ``attrs`` attributes.
    :param changes: Keyword changes in the new copy.

    :return: A copy of inst with *changes* incorporated.

    :raise attr.exceptions.AttrsAttributeNotFoundError: If *attr_name* couldn't
        be found on *cls*.
    :raise attr.exceptions.NotAnAttrsClassError: If *cls* is not an ``attrs``
        class.

    ..  deprecated:: 17.1.0
        Use :func:`evolve` instead.
    """
    import warnings

    warnings.warn(
        "assoc is deprecated and will be removed after 2018/01.",
        DeprecationWarning,
        stacklevel=2,
    )
    new = copy.copy(inst)
    attrs = fields(inst.__class__)
    for k, v in iteritems(changes):
        a = getattr(attrs, k, NOTHING)
        if a is NOTHING:
            raise AttrsAttributeNotFoundError(
                "{k} is not an attrs attribute on {cl}.".format(
                    k=k, cl=new.__class__
                )
            )
        _obj_setattr(new, k, v)
    return new