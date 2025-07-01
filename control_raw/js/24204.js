function i18nInterpolation6(instructions, v0, v1, v2, v3, v4, v5) {
    var different = bindingUpdated4(v0, v1, v2, v3);
    different = bindingUpdated2(v4, v5) || different;
    if (!different) {
        return NO_CHANGE;
    }
    var res = '';
    for (var i = 0; i < instructions.length; i++) {
        // Odd indexes are bindings
        if (i & 1) {
            // Extract bits
            var idx = instructions[i];
            var b4 = idx & 4;
            var b2 = idx & 2;
            var b1 = idx & 1;
            // Get the value from the argument vx where x = idx
            var value = b4 ? (b1 ? v5 : v4) : (b2 ? (b1 ? v3 : v2) : (b1 ? v1 : v0));
            res += stringify$1(value);
        }
        else {
            res += instructions[i];
        }
    }
    return res;
}