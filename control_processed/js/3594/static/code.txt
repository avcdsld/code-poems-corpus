function (controllerPosition) {
    // Use controllerPosition and deltaControllerPosition to avoid creating variables.
    var controller = this.controller;
    var controllerEuler = this.controllerEuler;
    var controllerQuaternion = this.controllerQuaternion;
    var deltaControllerPosition = this.deltaControllerPosition;
    var hand;
    var headEl;
    var headObject3D;
    var pose;
    var userHeight;

    headEl = this.getHeadElement();
    headObject3D = headEl.object3D;
    userHeight = this.defaultUserHeight();

    pose = controller.pose;
    hand = (controller ? controller.hand : undefined) || DEFAULT_HANDEDNESS;

    // Use camera position as head position.
    controllerPosition.copy(headObject3D.position);
    // Set offset for degenerate "arm model" to elbow.
    deltaControllerPosition.set(
      EYES_TO_ELBOW.x * (hand === 'left' ? -1 : hand === 'right' ? 1 : 0),
      EYES_TO_ELBOW.y,  // Lower than our eyes.
      EYES_TO_ELBOW.z);  // Slightly out in front.
    // Scale offset by user height.
    deltaControllerPosition.multiplyScalar(userHeight);
    // Apply camera Y rotation (not X or Z, so you can look down at your hand).
    deltaControllerPosition.applyAxisAngle(headObject3D.up, headObject3D.rotation.y);
    // Apply rotated offset to position.
    controllerPosition.add(deltaControllerPosition);

    // Set offset for degenerate "arm model" forearm. Forearm sticking out from elbow.
    deltaControllerPosition.set(FOREARM.x, FOREARM.y, FOREARM.z);
    // Scale offset by user height.
    deltaControllerPosition.multiplyScalar(userHeight);
    // Apply controller X/Y rotation (tilting up/down/left/right is usually moving the arm).
    if (pose.orientation) {
      controllerQuaternion.fromArray(pose.orientation);
    } else {
      controllerQuaternion.copy(headObject3D.quaternion);
    }
    controllerEuler.setFromQuaternion(controllerQuaternion);
    controllerEuler.set(controllerEuler.x, controllerEuler.y, 0);
    deltaControllerPosition.applyEuler(controllerEuler);
    // Apply rotated offset to position.
    controllerPosition.add(deltaControllerPosition);
  }