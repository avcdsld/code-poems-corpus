function(first, startLine, startCol) {
        var comment = this.readComment(first);

        return this.createToken(Tokens.COMMENT, comment, startLine, startCol);
    }