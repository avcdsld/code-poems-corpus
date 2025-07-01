def format_sympy_expr(sympy_expr, functions=None):
  """Convert sympy expression into a string which can be encoded.

  Args:
    sympy_expr: Any sympy expression tree or string.
    functions: Defines special functions. A dict mapping human readable string
        names, like "log", "exp", "sin", "cos", etc., to single chars. Each
        function gets a unique token, like "L" for "log".

  Returns:
    A string representation of the expression suitable for encoding as a
        sequence input.
  """
  if functions is None:
    functions = {}
  str_expr = str(sympy_expr)
  result = str_expr.replace(" ", "")
  for fn_name, char in six.iteritems(functions):
    result = result.replace(fn_name, char)
  return result