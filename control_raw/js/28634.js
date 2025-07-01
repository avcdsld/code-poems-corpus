function(self, callback) {
  if (self.cursorState.dead && self.cursorState.killed) {
    handleCallback(callback, new MongoError('cursor is dead'));
    return true;
  }

  return false;
}