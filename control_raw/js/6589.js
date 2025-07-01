function(target, targetOffset, offset, length) {
    return this.toBuffer().copy(target, targetOffset, offset, length);
  }