function sortedMerge(tokens, comments) {
    const result = [];
    let tokenIndex = 0;
    let commentIndex = 0;

    while (tokenIndex < tokens.length || commentIndex < comments.length) {
        if (commentIndex >= comments.length || tokenIndex < tokens.length && tokens[tokenIndex].range[0] < comments[commentIndex].range[0]) {
            result.push(tokens[tokenIndex++]);
        } else {
            result.push(comments[commentIndex++]);
        }
    }

    return result;
}