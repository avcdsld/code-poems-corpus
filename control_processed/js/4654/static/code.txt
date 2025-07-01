function moveNextToken(ctx, precise) {
        var eol = ctx.editor.getLine(ctx.pos.line).length;
        if (precise === undefined) {
            precise = true;
        }

        if (ctx.pos.ch >= eol || ctx.token.end >= eol) {
            //move down a line
            if (ctx.pos.line >= ctx.editor.lineCount() - 1) {
                return false; //at the bottom
            }
            ctx.pos.line++;
            ctx.pos.ch = 0;
        } else {
            ctx.pos.ch = ctx.token.end + 1;
        }
        ctx.token = getTokenAt(ctx.editor, ctx.pos, precise);
        return true;
    }