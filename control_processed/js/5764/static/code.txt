function explodeArray(xs) {
    return xs.reduce((accumulator, x) => {
        accumulator.push([x]);
        return accumulator;
    }, []);
}