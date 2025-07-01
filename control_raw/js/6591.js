function() {
    if (this.buffers.length) {
      var last = this.buffers[this.buffers.length - 1];
      if (!last.full) {
        return last;
      }
    }
    var buf = new ReadWriteBuf(this.bufSize);
    this.buffers.push(buf);
    return buf;
  }