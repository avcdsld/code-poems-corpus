function (sourceBuffer, aNode, tagNameVariable) {
        var tagName = aNode.tagName;

        if (tagName) {
            if (!autoCloseTags[tagName]) {
                sourceBuffer.joinString('</' + tagName + '>');
            }

            if (tagName === 'select') {
                sourceBuffer.addRaw('$selectValue = null;');
            }

            if (tagName === 'option') {
                sourceBuffer.addRaw('$optionValue = null;');
            }
        }
        else {
            sourceBuffer.joinString('</');
            sourceBuffer.joinRaw(tagNameVariable + ' || "div"');
            sourceBuffer.joinString('>');
        }
    }