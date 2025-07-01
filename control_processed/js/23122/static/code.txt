function Sweep(c, a) {
  _ASSERT && common.assert(typeof c === 'undefined');
  _ASSERT && common.assert(typeof a === 'undefined');
  this.localCenter = Vec2.zero();
  this.c = Vec2.zero();
  this.a = 0;
  this.alpha0 = 0;
  this.c0 = Vec2.zero();
  this.a0 = 0;
}