def eval(expr, parser='pandas', engine=None, truediv=True,
         local_dict=None, global_dict=None, resolvers=(), level=0,
         target=None, inplace=False):
    """Evaluate a Python expression as a string using various backends.

    The following arithmetic operations are supported: ``+``, ``-``, ``*``,
    ``/``, ``**``, ``%``, ``//`` (python engine only) along with the following
    boolean operations: ``|`` (or), ``&`` (and), and ``~`` (not).
    Additionally, the ``'pandas'`` parser allows the use of :keyword:`and`,
    :keyword:`or`, and :keyword:`not` with the same semantics as the
    corresponding bitwise operators.  :class:`~pandas.Series` and
    :class:`~pandas.DataFrame` objects are supported and behave as they would
    with plain ol' Python evaluation.

    Parameters
    ----------
    expr : str or unicode
        The expression to evaluate. This string cannot contain any Python
        `statements
        <https://docs.python.org/3/reference/simple_stmts.html#simple-statements>`__,
        only Python `expressions
        <https://docs.python.org/3/reference/simple_stmts.html#expression-statements>`__.
    parser : string, default 'pandas', {'pandas', 'python'}
        The parser to use to construct the syntax tree from the expression. The
        default of ``'pandas'`` parses code slightly different than standard
        Python. Alternatively, you can parse an expression using the
        ``'python'`` parser to retain strict Python semantics.  See the
        :ref:`enhancing performance <enhancingperf.eval>` documentation for
        more details.
    engine : string or None, default 'numexpr', {'python', 'numexpr'}

        The engine used to evaluate the expression. Supported engines are

        - None         : tries to use ``numexpr``, falls back to ``python``
        - ``'numexpr'``: This default engine evaluates pandas objects using
                         numexpr for large speed ups in complex expressions
                         with large frames.
        - ``'python'``: Performs operations as if you had ``eval``'d in top
                        level python. This engine is generally not that useful.

        More backends may be available in the future.

    truediv : bool, optional
        Whether to use true division, like in Python >= 3
    local_dict : dict or None, optional
        A dictionary of local variables, taken from locals() by default.
    global_dict : dict or None, optional
        A dictionary of global variables, taken from globals() by default.
    resolvers : list of dict-like or None, optional
        A list of objects implementing the ``__getitem__`` special method that
        you can use to inject an additional collection of namespaces to use for
        variable lookup. For example, this is used in the
        :meth:`~DataFrame.query` method to inject the
        ``DataFrame.index`` and ``DataFrame.columns``
        variables that refer to their respective :class:`~pandas.DataFrame`
        instance attributes.
    level : int, optional
        The number of prior stack frames to traverse and add to the current
        scope. Most users will **not** need to change this parameter.
    target : object, optional, default None
        This is the target object for assignment. It is used when there is
        variable assignment in the expression. If so, then `target` must
        support item assignment with string keys, and if a copy is being
        returned, it must also support `.copy()`.
    inplace : bool, default False
        If `target` is provided, and the expression mutates `target`, whether
        to modify `target` inplace. Otherwise, return a copy of `target` with
        the mutation.

    Returns
    -------
    ndarray, numeric scalar, DataFrame, Series

    Raises
    ------
    ValueError
        There are many instances where such an error can be raised:

        - `target=None`, but the expression is multiline.
        - The expression is multiline, but not all them have item assignment.
          An example of such an arrangement is this:

          a = b + 1
          a + 2

          Here, there are expressions on different lines, making it multiline,
          but the last line has no variable assigned to the output of `a + 2`.
        - `inplace=True`, but the expression is missing item assignment.
        - Item assignment is provided, but the `target` does not support
          string item assignment.
        - Item assignment is provided and `inplace=False`, but the `target`
          does not support the `.copy()` method

    See Also
    --------
    DataFrame.query
    DataFrame.eval

    Notes
    -----
    The ``dtype`` of any objects involved in an arithmetic ``%`` operation are
    recursively cast to ``float64``.

    See the :ref:`enhancing performance <enhancingperf.eval>` documentation for
    more details.
    """
    from pandas.core.computation.expr import Expr

    inplace = validate_bool_kwarg(inplace, "inplace")

    if isinstance(expr, str):
        _check_expression(expr)
        exprs = [e.strip() for e in expr.splitlines() if e.strip() != '']
    else:
        exprs = [expr]
    multi_line = len(exprs) > 1

    if multi_line and target is None:
        raise ValueError("multi-line expressions are only valid in the "
                         "context of data, use DataFrame.eval")

    ret = None
    first_expr = True
    target_modified = False

    for expr in exprs:
        expr = _convert_expression(expr)
        engine = _check_engine(engine)
        _check_parser(parser)
        _check_resolvers(resolvers)
        _check_for_locals(expr, level, parser)

        # get our (possibly passed-in) scope
        env = _ensure_scope(level + 1, global_dict=global_dict,
                            local_dict=local_dict, resolvers=resolvers,
                            target=target)

        parsed_expr = Expr(expr, engine=engine, parser=parser, env=env,
                           truediv=truediv)

        # construct the engine and evaluate the parsed expression
        eng = _engines[engine]
        eng_inst = eng(parsed_expr)
        ret = eng_inst.evaluate()

        if parsed_expr.assigner is None:
            if multi_line:
                raise ValueError("Multi-line expressions are only valid"
                                 " if all expressions contain an assignment")
            elif inplace:
                raise ValueError("Cannot operate inplace "
                                 "if there is no assignment")

        # assign if needed
        assigner = parsed_expr.assigner
        if env.target is not None and assigner is not None:
            target_modified = True

            # if returning a copy, copy only on the first assignment
            if not inplace and first_expr:
                try:
                    target = env.target.copy()
                except AttributeError:
                    raise ValueError("Cannot return a copy of the target")
            else:
                target = env.target

            # TypeError is most commonly raised (e.g. int, list), but you
            # get IndexError if you try to do this assignment on np.ndarray.
            # we will ignore numpy warnings here; e.g. if trying
            # to use a non-numeric indexer
            try:
                with warnings.catch_warnings(record=True):
                    # TODO: Filter the warnings we actually care about here.
                    target[assigner] = ret
            except (TypeError, IndexError):
                raise ValueError("Cannot assign expression output to target")

            if not resolvers:
                resolvers = ({assigner: ret},)
            else:
                # existing resolver needs updated to handle
                # case of mutating existing column in copy
                for resolver in resolvers:
                    if assigner in resolver:
                        resolver[assigner] = ret
                        break
                else:
                    resolvers += ({assigner: ret},)

            ret = None
            first_expr = False

    # We want to exclude `inplace=None` as being False.
    if inplace is False:
        return target if target_modified else ret