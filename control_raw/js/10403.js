function ShakaReceiver() {
  /** @private {HTMLMediaElement} */
  this.video_ = null;

  /** @private {shaka.Player} */
  this.player_ = null;

  /** @private {shaka.cast.CastReceiver} */
  this.receiver_ = null;

  /** @private {Element} */
  this.controlsElement_ = null;

  /** @private {?number} */
  this.controlsTimerId_ = null;

  /** @private {Element} */
  this.idle_ = null;

  /** @private {?number} */
  this.idleTimerId_ = null;

  /**
   * In seconds.
   * @const
   * @private {number}
   */
  this.idleTimeout_ = 300;
}