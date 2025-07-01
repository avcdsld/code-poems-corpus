def random_expr(depth, vlist, ops):
  """Generate a random expression tree.

  Args:
    depth: At least one leaf will be this many levels down from the top.
    vlist: A list of chars. These chars are randomly selected as leaf values.
    ops: A list of ExprOp instances.

  Returns:
    An ExprNode instance which is the root of the generated expression tree.
  """
  if not depth:
    return str(vlist[random.randrange(len(vlist))])

  max_depth_side = random.randrange(2)
  other_side_depth = random.randrange(depth)

  left = random_expr(depth - 1
                     if max_depth_side else other_side_depth, vlist, ops)
  right = random_expr(depth - 1
                      if not max_depth_side else other_side_depth, vlist, ops)

  op = ops[random.randrange(len(ops))]
  return ExprNode(left, right, op)