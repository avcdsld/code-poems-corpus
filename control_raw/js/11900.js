function convertToNumber(value) {
    if (_.isString(value)) {
        value = value.replace(/,/g, '');
    }

    if (_.isNumber(value) || isNaN(value) || util.isBlank(value)) {
        return value;
    }

    return Number(value);
}