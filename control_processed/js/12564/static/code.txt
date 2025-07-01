function readMultiplicativeExpr(walker) {
    var expr = readUnaryExpr(walker);

    while (1) {
        walker.goUntil();

        var code = walker.currentCode();
        switch (code) {
            case 37: // %
            case 42: // *
            case 47: // /
                walker.go(1);
                expr = {
                    type: ExprType.BINARY,
                    operator: code,
                    segs: [expr, readUnaryExpr(walker)]
                };
                continue;
        }

        break;
    }


    return expr;
}