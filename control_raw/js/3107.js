function() {
  this.lastTime = 0;

  // Setup our different game components.
  this.audio = new Sound();
  this.player = new Player(10, 26, Math.PI * 1.9, 2.5);
  this.controls = new Controls();
  this.map = new Map(25);
  this.camera = new Camera(isMobile ? 256 : 512);
  
  requestAnimationFrame(this.tick.bind(this));
}