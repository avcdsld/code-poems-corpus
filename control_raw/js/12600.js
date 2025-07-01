function (aNode, sourceBuffer, owner) {
        elementSourceCompiler.tagStart(sourceBuffer, aNode);
        elementSourceCompiler.inner(sourceBuffer, aNode, owner);
        elementSourceCompiler.tagEnd(sourceBuffer, aNode);
    }