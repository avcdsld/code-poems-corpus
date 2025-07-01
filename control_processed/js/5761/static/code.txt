function hasJSDocThisTag(node, sourceCode) {
    const jsdocComment = sourceCode.getJSDocComment(node);

    if (jsdocComment && thisTagPattern.test(jsdocComment.value)) {
        return true;
    }

    // Checks `@this` in its leading comments for callbacks,
    // because callbacks don't have its JSDoc comment.
    // e.g.
    //     sinon.test(/* @this sinon.Sandbox */function() { this.spy(); });
    return sourceCode.getCommentsBefore(node).some(comment => thisTagPattern.test(comment.value));
}