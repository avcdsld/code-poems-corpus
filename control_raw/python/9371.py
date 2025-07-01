def emitCurrentToken(self):
        """This method is a generic handler for emitting the tags. It also sets
        the state to "data" because that's what's needed after a token has been
        emitted.
        """
        token = self.currentToken
        # Add token to the queue to be yielded
        if (token["type"] in tagTokenTypes):
            token["name"] = token["name"].translate(asciiUpper2Lower)
            if token["type"] == tokenTypes["EndTag"]:
                if token["data"]:
                    self.tokenQueue.append({"type": tokenTypes["ParseError"],
                                            "data": "attributes-in-end-tag"})
                if token["selfClosing"]:
                    self.tokenQueue.append({"type": tokenTypes["ParseError"],
                                            "data": "self-closing-flag-on-end-tag"})
        self.tokenQueue.append(token)
        self.state = self.dataState