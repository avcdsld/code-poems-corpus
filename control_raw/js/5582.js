function isCommentAtBlockEnd(token) {
            return isCommentAtParentEnd(token, "ClassBody") || isCommentAtParentEnd(token, "BlockStatement") || isCommentAtParentEnd(token, "SwitchCase") || isCommentAtParentEnd(token, "SwitchStatement");
        }