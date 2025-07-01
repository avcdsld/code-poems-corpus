function classify(str) {
    return str
        .split('.')
        .map(part => capitalize(camelize(part)))
        .join('.');
}