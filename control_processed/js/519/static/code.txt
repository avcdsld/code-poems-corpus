function prunning(node, clipRect, viewAbovePath, viewRoot, depth) {
    var nodeLayout = node.getLayout();
    var nodeInViewAbovePath = viewAbovePath[depth];
    var isAboveViewRoot = nodeInViewAbovePath && nodeInViewAbovePath === node;

    if (
        (nodeInViewAbovePath && !isAboveViewRoot)
        || (depth === viewAbovePath.length && node !== viewRoot)
    ) {
        return;
    }

    node.setLayout({
        // isInView means: viewRoot sub tree + viewAbovePath
        isInView: true,
        // invisible only means: outside view clip so that the node can not
        // see but still layout for animation preparation but not render.
        invisible: !isAboveViewRoot && !clipRect.intersect(nodeLayout),
        isAboveViewRoot: isAboveViewRoot
    }, true);

    // Transform to child coordinate.
    var childClipRect = new BoundingRect(
        clipRect.x - nodeLayout.x,
        clipRect.y - nodeLayout.y,
        clipRect.width,
        clipRect.height
    );

    each(node.viewChildren || [], function (child) {
        prunning(child, childClipRect, viewAbovePath, viewRoot, depth + 1);
    });
}