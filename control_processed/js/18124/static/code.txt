function Animation(prefabCount, prefabSize, bounds) {
  this.bounds = bounds;

  // create a prefab
  var prefab = new THREE.PlaneGeometry(prefabSize, prefabSize, 1, 8);

  // create a geometry where the prefab is repeated 'prefabCount' times
  var geometry = new NuggetCollisionGeometry(prefab, prefabCount);
  
  // animation timing

  // each prefab has a start time (delay) and duration
  var aDelayDuration = geometry.createAttribute('aDelayDuration', 2);
  var delay;
  var duration;
  var minDuration = 0.25;
  var maxDuration = 1.0;
  var prefabDelay = 0.0;
  var vertexDelay = 0.01;

  for (var i = 0, offset = 0; i < prefabCount; i++) {
    delay = prefabDelay * i;
    duration = THREE.Math.randFloat(minDuration, maxDuration);
    
    for (var j = 0; j < geometry.prefabVertexCount; j++) {
      // by giving EACH VERTEX in a prefab its own delay (based on index) the prefabs are stretched out
      // as the animation plays
      aDelayDuration.array[offset++] = delay + vertexDelay * duration * j;
      aDelayDuration.array[offset++] = duration;
    }
  }
  
  this.totalDuration = maxDuration + prefabDelay * prefabCount + vertexDelay * geometry.prefabVertexCount;

  // position

  // start position is always (0, 0, 0)
  // this attribute could be removed, but I've kept it around for consistency
  geometry.createAttribute('aStartPosition', 3);
  // control positions and end position are filled inside the 'bufferPoints' method below
  geometry.createAttribute('aControlPosition0', 3);
  geometry.createAttribute('aControlPosition1', 3);
  geometry.createAttribute('aEndPosition', 3);

  // color

  // each prefab will have a tint of the gold-ish color #d7d2bf
  var colorObj = new THREE.Color('#d7d2bf');
  var colorHSL = colorObj.getHSL();
  var h, s, l;
  
  geometry.createAttribute('color', 3, function(data) {
    h = colorHSL.h;
    s = colorHSL.s;
    l = THREE.Math.randFloat(0.25, 1.00);
    colorObj.setHSL(h, s, l);
    
    colorObj.toArray(data);
  });
  
  // rotation
  
  var axis = new THREE.Vector3();
  
  geometry.createAttribute('aAxisAngle', 4, function(data) {
    BAS.Utils.randomAxis(axis).toArray(data);
    data[3] = Math.PI * THREE.Math.randFloat(8, 16);
  });
  
  var material = new BAS.BasicAnimationMaterial({
    side: THREE.DoubleSide,
    vertexColors: THREE.VertexColors,
    transparent: true,
    uniforms: {
      uTime: {value: 0.0}
    },
    vertexFunctions: [
      BAS.ShaderChunk['quaternion_rotation'],
      BAS.ShaderChunk['cubic_bezier'],
      BAS.ShaderChunk['ease_cubic_out']
    ],
    vertexParameters: [
      'uniform float uTime;',
  
      'attribute vec2 aDelayDuration;',
      'attribute vec3 aStartPosition;',
      'attribute vec3 aControlPosition0;',
      'attribute vec3 aControlPosition1;',
      'attribute vec3 aEndPosition;',
      'attribute vec4 aAxisAngle;'
    ],
    vertexPosition: [
      'float tProgress = clamp(uTime - aDelayDuration.x, 0.0, aDelayDuration.y) / aDelayDuration.y;',
      'tProgress = easeCubicOut(tProgress);',

      // rotate
      'vec4 tQuat = quatFromAxisAngle(aAxisAngle.xyz, aAxisAngle.w * tProgress);',
      'transformed = rotateVector(tQuat, transformed);',

      // scale (0.0 at start, 1.0 halfway, 0.0 at end of progress)
      'float scl = tProgress * 2.0 - 1.0;',
      'transformed *= (1.0 - scl * scl);',

      // translate
      'transformed += cubicBezier(aStartPosition, aControlPosition0, aControlPosition1, aEndPosition, tProgress);'
    ]
  });

  THREE.Mesh.call(this, geometry, material);
  this.frustumCulled = false;
  
  this.tween = TweenMax.fromTo(this.material.uniforms['uTime'], 1.0, {value: 0}, {
    value:this.totalDuration,
    ease:Power0.easeOut,
    onCompleteScope: this,
    onComplete: function() {
      this.dispatchEvent({type: 'tween_complete'});
    }
  });
  this.tween.pause();
}