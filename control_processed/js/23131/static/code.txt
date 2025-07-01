function Joint(def, bodyA, bodyB) {
  bodyA = def.bodyA || bodyA;
  bodyB = def.bodyB || bodyB;

  _ASSERT && common.assert(bodyA);
  _ASSERT && common.assert(bodyB);
  _ASSERT && common.assert(bodyA != bodyB);

  this.m_type = 'unknown-joint';

  this.m_bodyA = bodyA;
  this.m_bodyB = bodyB;

  this.m_index = 0;
  this.m_collideConnected = !!def.collideConnected;

  this.m_prev = null;
  this.m_next = null;

  this.m_edgeA = new JointEdge();
  this.m_edgeB = new JointEdge();

  this.m_islandFlag = false;
  this.m_userData = def.userData;
}