function getBinaryMapWithDepth(depth) {
  var mm = new mindmaps.MindMap();
  var root = mm.root;

  function createTwoChildren(node, depth) {
    if (depth === 0) {
      return;
    }

    var left = mm.createNode();
    left.text.caption = "Node " + left.id;
    node.addChild(left);
    createTwoChildren(left, depth - 1);

    var right = mm.createNode();
    right.text.caption = "Node " + right.id;
    node.addChild(right);
    createTwoChildren(right, depth - 1);
  }

  // depth 10: about 400kb, 800kb in chrome
  // depth 12: about 1600kb
  // depth 16: 25mb
  var depth = depth || 10;
  createTwoChildren(root, depth);

  // generate positions for all nodes.
  // tree grows balanced from left to right
  root.offset = new mindmaps.Point(400, 400);
  // var offset = Math.pow(2, depth-1) * 10;
  var offset = 80;
  var c = root.children.values();
  setOffset(c[0], 0, -offset);
  setOffset(c[1], 0, offset);
  function setOffset(node, depth, offsetY) {
    node.offset = new mindmaps.Point((depth + 1) * 50, offsetY);

    if (node.isLeaf()) {
      return;
    }

    var c = node.children.values();
    var left = c[0];
    setOffset(left, depth + 1, offsetY - offsetY / 2);

    var right = c[1];
    setOffset(right, depth + 1, offsetY + offsetY / 2);
  }

  // color nodes
  c[0].branchColor = mindmaps.Util.randomColor();
  c[0].forEachDescendant(function(node) {
    node.branchColor = mindmaps.Util.randomColor();
  });
  c[1].branchColor = mindmaps.Util.randomColor();
  c[1].forEachDescendant(function(node) {
    node.branchColor = mindmaps.Util.randomColor();
  });

  return mm;
}