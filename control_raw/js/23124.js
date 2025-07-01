function RopeJoint(def, bodyA, bodyB, anchor) {
  if (!(this instanceof RopeJoint)) {
    return new RopeJoint(def, bodyA, bodyB, anchor);
  }

  def = options(def, DEFAULTS);
  Joint.call(this, def, bodyA, bodyB);
  bodyA = this.m_bodyA;
  bodyB = this.m_bodyB;

  this.m_type = RopeJoint.TYPE;
  this.m_localAnchorA = anchor ? bodyA.getLocalPoint(anchor) : def.localAnchorA || Vec2.neo(-1.0, 0.0);
  this.m_localAnchorB = anchor ? bodyB.getLocalPoint(anchor) : def.localAnchorB || Vec2.neo(1.0, 0.0);

  this.m_maxLength = def.maxLength;

  this.m_mass = 0.0;
  this.m_impulse = 0.0;
  this.m_length = 0.0;
  this.m_state = inactiveLimit;

  // Solver temp
  this.m_u; // Vec2
  this.m_rA; // Vec2
  this.m_rB; // Vec2
  this.m_localCenterA; // Vec2
  this.m_localCenterB; // Vec2
  this.m_invMassA; // float
  this.m_invMassB; // float
  this.m_invIA; // float
  this.m_invIB; // float
  this.m_mass; // float

  // Limit:
  // C = norm(pB - pA) - L
  // u = (pB - pA) / norm(pB - pA)
  // Cdot = dot(u, vB + cross(wB, rB) - vA - cross(wA, rA))
  // J = [-u -cross(rA, u) u cross(rB, u)]
  // K = J * invM * JT
  // = invMassA + invIA * cross(rA, u)^2 + invMassB + invIB * cross(rB, u)^2
}