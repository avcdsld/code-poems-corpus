function Manifold() {
  this.type;
  this.localNormal = Vec2.zero();
  this.localPoint = Vec2.zero();
  this.points = [ new ManifoldPoint(), new ManifoldPoint() ];
  this.pointCount = 0;
}