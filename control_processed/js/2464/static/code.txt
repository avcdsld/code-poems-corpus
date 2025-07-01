function some(arr, iter) {
    arr = Immutable.List(arr);

    return arr.reduce(function(prev, elem, i) {
        return prev.then(function(val) {
            if (val) return val;

            return iter(elem, i);
        });
    }, Q());
}