function block(ordinary, stmt, isfunc, isfatarrow, iscase) {
    var a,
      b = inblock,
      old_indent = indent,
      m,
      s = scope,
      t,
      line,
      d;

    inblock = ordinary;

    if (!ordinary || !state.option.funcscope)
      scope = Object.create(scope);

    t = state.tokens.next;

    var metrics = funct["(metrics)"];
    metrics.nestedBlockDepth += 1;
    metrics.verifyMaxNestedBlockDepthPerFunction();

    if (state.tokens.next.id === "{") {
      advance("{");

      // create a new block scope
      funct["(blockscope)"].stack();

      line = state.tokens.curr.line;
      if (state.tokens.next.id !== "}") {
        indent += state.option.indent;
        while (!ordinary && state.tokens.next.from > indent) {
          indent += state.option.indent;
        }

        if (isfunc) {
          m = {};
          for (d in state.directive) {
            if (_.has(state.directive, d)) {
              m[d] = state.directive[d];
            }
          }
          directives();

          if (state.option.strict && funct["(context)"]["(global)"]) {
            if (!m["use strict"] && !state.directive["use strict"]) {
              warning("E007");
            }
          }
        }

        a = statements(line);

        metrics.statementCount += a.length;

        if (isfunc) {
          state.directive = m;
        }

        indent -= state.option.indent;
      }

      advance("}", t);

      funct["(blockscope)"].unstack();

      indent = old_indent;
    } else if (!ordinary) {
      if (isfunc) {
        m = {};
        if (stmt && !isfatarrow && !state.option.inMoz(true)) {
          error("W118", state.tokens.curr, "function closure expressions");
        }

        if (!stmt) {
          for (d in state.directive) {
            if (_.has(state.directive, d)) {
              m[d] = state.directive[d];
            }
          }
        }
        expression(10);

        if (state.option.strict && funct["(context)"]["(global)"]) {
          if (!m["use strict"] && !state.directive["use strict"]) {
            warning("E007");
          }
        }
      } else {
        error("E021", state.tokens.next, "{", state.tokens.next.value);
      }
    } else {

      // check to avoid let declaration not within a block
      funct["(nolet)"] = true;

      if (!stmt || state.option.curly) {
        warning("W116", state.tokens.next, "{", state.tokens.next.value);
      }

      noreach = true;
      indent += state.option.indent;
      // test indentation only if statement is in new line
      a = [statement()];
      indent -= state.option.indent;
      noreach = false;

      delete funct["(nolet)"];
    }

    // Don't clear and let it propagate out if it is "break", "return" or similar in switch case
    switch (funct["(verb)"]) {
    case "break":
    case "continue":
    case "return":
    case "throw":
      if (iscase) {
        break;
      }

      /* falls through */
    default:
      funct["(verb)"] = null;
    }

    if (!ordinary || !state.option.funcscope) scope = s;
    inblock = b;
    if (ordinary && state.option.noempty && (!a || a.length === 0)) {
      warning("W035");
    }
    metrics.nestedBlockDepth -= 1;
    return a;
  }