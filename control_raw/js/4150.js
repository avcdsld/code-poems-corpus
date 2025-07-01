function _onRemoteShowGoto(event, res) {
        // res = {nodeId, name, value}
        var node = DOMAgent.nodeWithId(res.nodeId);

        // get all css rules that apply to the given node
        Inspector.CSS.getMatchedStylesForNode(node.nodeId, function onMatchedStyles(res) {
            var i, targets = [];
            _makeHTMLTarget(targets, node);
            for (i in node.trace) {
                _makeJSTarget(targets, node.trace[i]);
            }
            for (i in node.events) {
                var trace = node.events[i];
                _makeJSTarget(targets, trace.callFrames[0]);
            }
            for (i in res.matchedCSSRules.reverse()) {
                _makeCSSTarget(targets, res.matchedCSSRules[i].rule);
            }
            RemoteAgent.call("showGoto", targets);
        });
    }