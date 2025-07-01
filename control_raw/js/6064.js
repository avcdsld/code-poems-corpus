function addNullElementsToIgnoreList(node) {
            let previousToken = sourceCode.getFirstToken(node);

            node.elements.forEach(element => {
                let token;

                if (element === null) {
                    token = sourceCode.getTokenAfter(previousToken);

                    if (astUtils.isCommaToken(token)) {
                        commaTokensToIgnore.push(token);
                    }
                } else {
                    token = sourceCode.getTokenAfter(element);
                }

                previousToken = token;
            });
        }