function TreeNode(id) {
  this.id = id;
  this.aabb = new AABB();
  this.userData = null;
  this.parent = null;
  this.child1 = null;
  this.child2 = null;
  this.height = -1;

  this.toString = function() {
    return this.id + ": " + this.userData;
  }
}