function relaxRightToLeft(nodesByBreadth, alpha, orient) {
    zrUtil.each(nodesByBreadth.slice().reverse(), function (nodes) {
        zrUtil.each(nodes, function (node) {
            if (node.outEdges.length) {
                var y = sum(node.outEdges, weightedTarget, orient)
                        / sum(node.outEdges, getEdgeValue, orient);
                if (orient === 'vertical') {
                    var nodeX = node.getLayout().x + (y - center(node, orient)) * alpha;
                    node.setLayout({x: nodeX}, true);
                }
                else {
                    var nodeY = node.getLayout().y + (y - center(node, orient)) * alpha;
                    node.setLayout({y: nodeY}, true);
                }
            }
        });
    });
}