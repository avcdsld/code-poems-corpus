function SymmetricallyEncrypted() {
  /**
   * Packet type
   * @type {module:enums.packet}
   */
  this.tag = enums.packet.symmetricallyEncrypted;
  /**
   * Encrypted secret-key data
   */
  this.encrypted = null;
  /**
   * Decrypted packets contained within.
   * @type {module:packet.List}
   */
  this.packets = null;
  /**
   * When true, decrypt fails if message is not integrity protected
   * @see module:config.ignore_mdc_error
   */
  this.ignore_mdc_error = config.ignore_mdc_error;
}