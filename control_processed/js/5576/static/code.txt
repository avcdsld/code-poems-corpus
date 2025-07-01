function getEmptyLineNums(lines) {
    const emptyLines = lines.map((line, i) => ({
        code: line.trim(),
        num: i + 1
    })).filter(line => !line.code).map(line => line.num);

    return emptyLines;
}