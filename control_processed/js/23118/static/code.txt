function Contact(fA, indexA, fB, indexB, evaluateFcn) {
  // Nodes for connecting bodies.
  this.m_nodeA = new ContactEdge(this);
  this.m_nodeB = new ContactEdge(this);

  this.m_fixtureA = fA;
  this.m_fixtureB = fB;

  this.m_indexA = indexA;
  this.m_indexB = indexB;

  this.m_evaluateFcn = evaluateFcn;

  this.m_manifold = new Manifold();

  this.m_prev = null;
  this.m_next = null;

  this.m_toi = 1.0;
  this.m_toiCount = 0;
  // This contact has a valid TOI in m_toi
  this.m_toiFlag = false;

  this.m_friction = mixFriction(this.m_fixtureA.m_friction,
      this.m_fixtureB.m_friction);
  this.m_restitution = mixRestitution(this.m_fixtureA.m_restitution,
      this.m_fixtureB.m_restitution);

  this.m_tangentSpeed = 0.0;

  // This contact can be disabled (by user)
  this.m_enabledFlag = true;

  // Used when crawling contact graph when forming islands.
  this.m_islandFlag = false;

  // Set when the shapes are touching.
  this.m_touchingFlag = false;

  // This contact needs filtering because a fixture filter was changed.
  this.m_filterFlag = false;

  // This bullet contact had a TOI event
  this.m_bulletHitFlag = false;

  this.v_points = []; // VelocityConstraintPoint[maxManifoldPoints]
  this.v_normal = Vec2.zero();
  this.v_normalMass = new Mat22();
  this.v_K = new Mat22();
  this.v_pointCount;

  this.v_tangentSpeed;
  this.v_friction;
  this.v_restitution;

  this.v_invMassA;
  this.v_invMassB;
  this.v_invIA;
  this.v_invIB;

  this.p_localPoints = [] // Vec2[maxManifoldPoints];
  this.p_localNormal = Vec2.zero();
  this.p_localPoint = Vec2.zero();
  this.p_localCenterA = Vec2.zero();
  this.p_localCenterB = Vec2.zero();
  this.p_type; // Manifold.Type
  this.p_radiusA;
  this.p_radiusB;
  this.p_pointCount;

  this.p_invMassA;
  this.p_invMassB;
  this.p_invIA;
  this.p_invIB;
}