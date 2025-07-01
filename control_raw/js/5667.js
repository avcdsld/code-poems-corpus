function checkLastReturnStatementLineIndent(node, firstLineIndent) {

            /*
             * in case if return statement ends with ');' we have traverse back to ')'
             * otherwise we'll measure indent for ';' and replace ')'
             */
            const lastToken = sourceCode.getLastToken(node, astUtils.isClosingParenToken);
            const textBeforeClosingParenthesis = sourceCode.getText(lastToken, lastToken.loc.start.column).slice(0, -1);

            if (textBeforeClosingParenthesis.trim()) {

                // There are tokens before the closing paren, don't report this case
                return;
            }

            const endIndent = getNodeIndent(lastToken, true);

            if (endIndent.goodChar !== firstLineIndent) {
                report(
                    node,
                    firstLineIndent,
                    endIndent.space,
                    endIndent.tab,
                    { line: lastToken.loc.start.line, column: lastToken.loc.start.column },
                    true
                );
            }
        }