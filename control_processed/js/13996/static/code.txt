function(terria, scene, handler, keyboardModifier) {
  this._terria = terria;
  this._scene = scene;
  this._ellipsoid = scene.globe.ellipsoid;
  this._finishHandler = handler;
  this._mouseHandler = new ScreenSpaceEventHandler(scene.canvas, false);
  this._stopHandler = undefined;
  this._interHandler = undefined;
  this._dataSource = undefined;
  this._click1 = undefined;
  this._click2 = undefined;
  this.active = false;
  this.keyboardModifier = defaultValue(
    keyboardModifier,
    KeyboardEventModifier.SHIFT
  );
}