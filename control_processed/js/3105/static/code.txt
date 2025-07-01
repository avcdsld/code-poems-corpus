function(dist) {
    var dx = Math.cos(this.dir) * dist;
    var dy = Math.sin(this.dir) * dist;

    // Move the player if they can walk here.
    this.x += (game.map.check(this.x + dx, this.y) <= 0) ? dx : 0;
    this.y += (game.map.check(this.x, this.y + dy) <= 0) ? dy : 0;

    this.steps += dist;

    // Update the position of the audio listener.
    Howler.pos(this.x, this.y, -0.5);
  }