def algebra_inverse_solve(left, right, var, solve_ops):
  """Solves for the value of the given var in an expression.

  Args:
    left: The root of the ExprNode tree on the left side of the equals sign.
    right: The root of the ExprNode tree on the right side of the equals sign.
    var: A char. The variable to solve for.
    solve_ops: A dictionary with the following properties.
        * For each operator in the expression, there is a rule that determines
          how to cancel out a value either to the left or the right of that
          operator.
        * For each rule, there is an entry in the dictionary. The key is two
          chars- the op char, and either 'l' or 'r' meaning rule for canceling
          out the left or right sides. For example, '+l', '+r', '-l', '-r'.
        * The value of each entry is a function with the following signature:
          (left, right, to_tree) -> (new_from_tree, new_to_tree)
          left- Expression on left side of the op.
          right- Expression on the right side of the op.
          to_tree- The tree on the other side of the equal sign. The canceled
              out expression will be moved here.
          new_from_tree- The resulting from_tree after the algebraic
              manipulation.
          new_to_tree- The resulting to_tree after the algebraic manipulation.

  Returns:
    The root of an ExprNode tree which holds the value of `var` after solving.

  Raises:
    ValueError: If `var` does not appear exactly once in the equation (which
        includes the left and right sides).
  """
  is_in_left = is_in_expr(left, var)
  is_in_right = is_in_expr(right, var)
  if is_in_left == is_in_right:
    if is_in_left:
      raise ValueError("Solve-variable '%s' is on both sides of the equation. "
                       "Only equations where the solve variable-appears once "
                       "are supported by this solver. Left: '%s', right: '%s'" %
                       (var, str(left), str(right)))
    else:
      raise ValueError("Solve-variable '%s' is not present in the equation. It "
                       "must appear once. Left: '%s', right: '%s'" %
                       (var, str(left), str(right)))

  from_tree = left if is_in_left else right
  to_tree = left if not is_in_left else right
  while from_tree != var:
    is_in_left = is_in_expr(from_tree.left, var)
    is_in_right = is_in_expr(from_tree.right, var)
    from_tree, to_tree = (solve_ops[str(from_tree.op)
                                    + ("l" if is_in_left else "r")](
                                        from_tree.left, from_tree.right,
                                        to_tree))
  return to_tree