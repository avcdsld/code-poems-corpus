function getKeyWidth(property) {
            const startToken = sourceCode.getFirstToken(property);
            const endToken = getLastTokenBeforeColon(property.key);

            return endToken.range[1] - startToken.range[0];
        }