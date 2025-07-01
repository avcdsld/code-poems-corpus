function (aNode, sourceBuffer, owner, extra) {
        extra = extra || {};
        var compileMethod = 'compileElement';

        if (aNode.textExpr) {
            compileMethod = 'compileText';
        }
        else if (aNode.directives['if']) { // eslint-disable-line dot-notation
            compileMethod = 'compileIf';
        }
        else if (aNode.directives['for']) { // eslint-disable-line dot-notation
            compileMethod = 'compileFor';
        }
        else if (aNode.tagName === 'slot') {
            compileMethod = 'compileSlot';
        }
        else if (aNode.tagName === 'template') {
            compileMethod = 'compileTemplate';
        }
        else {
            var ComponentType = owner.getComponentType
                ? owner.getComponentType(aNode)
                : owner.components[aNode.tagName];

            if (ComponentType) {
                compileMethod = 'compileComponent';
                extra.ComponentClass = ComponentType;

                if (ComponentType instanceof ComponentLoader) {
                    compileMethod = 'compileComponentLoader';
                }
            }
        }

        aNodeCompiler[compileMethod](aNode, sourceBuffer, owner, extra);
    }