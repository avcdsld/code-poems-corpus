function readNumericString(s, minValue) {
    var length = readLength(s);
    length = (length + minValue + 1) / 2;
    s.readPadding(length);
}