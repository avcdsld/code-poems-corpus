function isFirstTokenInCurrentLine(token) {
            const tokenBefore = sourceCode.getTokenBefore(token);

            return !(tokenBefore && astUtils.isTokenOnSameLine(token, tokenBefore));
        }