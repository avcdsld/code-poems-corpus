function _getFunctionEndOffset(text, offsetStart) {
        var mode = CodeMirror.getMode({}, "javascript");
        var state = CodeMirror.startState(mode), stream, style, token;
        var curOffset = offsetStart, length = text.length, blockCount = 0, lineStart;
        var foundStartBrace = false;

        // Get a stream for the next line, and update curOffset and lineStart to point to the
        // beginning of that next line. Returns false if we're at the end of the text.
        function nextLine() {
            if (stream) {
                curOffset++; // account for \n
                if (curOffset >= length) {
                    return false;
                }
            }
            lineStart = curOffset;
            var lineEnd = text.indexOf("\n", lineStart);
            if (lineEnd === -1) {
                lineEnd = length;
            }
            stream = new CodeMirror.StringStream(text.slice(curOffset, lineEnd));
            return true;
        }

        // Get the next token, updating the style and token to refer to the current
        // token, and updating the curOffset to point to the end of the token (relative
        // to the start of the original text).
        function nextToken() {
            if (curOffset >= length) {
                return false;
            }
            if (stream) {
                // Set the start of the next token to the current stream position.
                stream.start = stream.pos;
            }
            while (!stream || stream.eol()) {
                if (!nextLine()) {
                    return false;
                }
            }
            style = mode.token(stream, state);
            token = stream.current();
            curOffset = lineStart + stream.pos;
            return true;
        }

        while (nextToken()) {
            if (style !== "comment" && style !== "regexp" && style !== "string" && style !== "string-2") {
                if (token === "{") {
                    foundStartBrace = true;
                    blockCount++;
                } else if (token === "}") {
                    blockCount--;
                }
            }

            // blockCount starts at 0, so we don't want to check if it hits 0
            // again until we've actually gone past the start of the function body.
            if (foundStartBrace && blockCount <= 0) {
                return curOffset;
            }
        }

        // Shouldn't get here, but if we do, return the end of the text as the offset.
        return length;
    }